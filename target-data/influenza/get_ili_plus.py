import pandas as pd 
import numpy as np
from datetime import datetime, timedelta

def compute_positivity(grp): 
    tests = grp.loc[grp.indicator == "tests"]
    detections = grp.loc[grp.indicator == "detections"]

    if tests.shape[0] > 0 and detections.shape[0] > 0:
        return detections.value.values[0] / tests.value.values[0]
    else: 
        return np.nan

def get_sunday_of_week(year_week):
    # Create a datetime object for the first day of the week
    first_day = datetime.strptime(f'{year_week}-1', "%Y-W%W-%w")
    # Calculate the number of days to Sunday (6 represents Sunday)
    days_to_sunday = (6 - first_day.weekday()) % 7
    # Add the number of days to get the Sunday of that week
    sunday = first_day + timedelta(days=days_to_sunday)
    return sunday

# countries that reported less than 50% sentinel points in 2023/2024
non_sentinel_countries = ['Malta', 'Iceland', 'Croatia', 'Romania', 'Latvia', 'Finland']

# import iso codes
iso_df = pd.read_csv("../../supporting-files/locations_iso2_codes.csv")
iso_df.sort_values(by="location_name", inplace=True, ignore_index=True)

# import ILI data 
df = pd.read_csv("https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/ILIARIRates.csv")
df_ili = df.loc[df.indicator == "ILIconsultationrate"]

# import non-sentinel detections
df_non_sentinel = pd.read_csv("https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/nonSentinelTestsDetections.csv")
df_non_sentinel = df_non_sentinel.loc[(df_non_sentinel.pathogen == "Influenza") & \
                                       (df_non_sentinel.pathogensubtype == "total")]

# import sentinel detections
df_sentinel = pd.read_csv("https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/sentinelTestsDetectionsPositivity.csv")
df_sentinel = df_sentinel.loc[(df_sentinel.pathogen == "Influenza") & \
                              (df_sentinel.pathogensubtype == "total")]

# compute positivity
df_sentinel = df_sentinel.groupby(["countryname", "yearweek"], as_index=False).apply(compute_positivity)
df_sentinel.rename(columns={None: "sentinel_positivity"}, inplace=True)
df_non_sentinel = df_non_sentinel.groupby(["countryname", "yearweek"], as_index=False).apply(compute_positivity)
df_non_sentinel.rename(columns={None: "non_sentinel_positivity"}, inplace=True)
df_positivity = pd.merge(df_non_sentinel, df_sentinel, on=["countryname", "yearweek"])

# merge and compute ILI+
df_total = pd.merge(df_ili, df_positivity, on=["countryname", "yearweek"], how="left")
df_total["value_adjusted_sentinel"] = df_total["value"] * df_total["sentinel_positivity"]
df_total["value_adjusted_non_sentinel"] = df_total["value"] * df_total["non_sentinel_positivity"]

# format and add info on date, country
df_total.rename(columns={"countryname": "location_name"}, inplace=True)
df_total["week_end_date"] = df_total.yearweek.apply(get_sunday_of_week)

# merge iso2 codes
df_total = df_total.merge(iso_df, on="location_name", how="left")
df_total = df_total[["location_name", "iso2_code", "yearweek", "week_end_date", "age", "value_adjusted_sentinel", "value_adjusted_non_sentinel"]]

# choose sentinel or non-sentinel data
df_final_sentinel = df_total.loc[~df_total.location_name.isin(non_sentinel_countries)]
df_final_sentinel.drop(columns=["value_adjusted_non_sentinel"], axis=1, inplace=True)
df_final_sentinel.rename(columns={"value_adjusted_sentinel": "value"}, inplace=True)
df_final_sentinel["source"] = "sentinel"

df_final_non_sentinel = df_total.loc[df_total.location_name.isin(non_sentinel_countries)]
df_final_non_sentinel.drop(columns=["value_adjusted_sentinel"], axis=1, inplace=True)
df_final_non_sentinel.rename(columns={"value_adjusted_non_sentinel": "value"}, inplace=True)
df_final_non_sentinel["source"] = "non_sentinel"

df_final = pd.concat([df_final_sentinel, df_final_non_sentinel], ignore_index=True)
df_final.to_csv("ili_plus.csv", index=False)
