# %%
import pandas as pd
from datetime import datetime, timedelta

def get_sunday_of_week(year_week):
    # Create a datetime object for the first day of the week
    first_day = datetime.strptime(f'{year_week}-1', "%Y-W%W-%w")
    # Calculate the number of days to Sunday (6 represents Sunday)
    days_to_sunday = (6 - first_day.weekday()) % 7
    # Add the number of days to get the Sunday of that week
    sunday = first_day + timedelta(days=days_to_sunday)
    return sunday

# import iso2 
iso_df = pd.read_csv('../../../supporting-files/locations_iso2_codes.csv')

# import non-sentinel data 
non_sentinel_df = pd.read_csv('https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/nonSentinelTestsDetections.csv')

# import sentinel data
sentinel_df = pd.read_csv('https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/sentinelTestsDetectionsPositivity.csv')

# concat 
df = pd.concat([non_sentinel_df, sentinel_df], ignore_index=True)

# add iso2 codes
df.rename(columns={"countryname": "location_name"}, inplace=True)
df = df.merge(iso_df, on='location_name', how='left')

# add date 
df["week_end_date"] = df.yearweek.apply(get_sunday_of_week)
df = df[['survtype', 'location_name', 'iso2_code', 'yearweek', 'week_end_date', 'pathogen', 'pathogentype','pathogensubtype', 'indicator', 'age', 'value']]

# save 
df.to_csv("./pathogen_detection.csv", index=False)

# %%



