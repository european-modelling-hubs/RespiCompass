import pandas as pd 
from datetime import datetime, timedelta
import argparse 
import os

def get_sunday_of_week(year_week):
    # Create a datetime object for the first day of the week
    first_day = datetime.strptime(f'{year_week}-1', "%Y-W%W-%w")
    # Calculate the number of days to Sunday (6 represents Sunday)
    days_to_sunday = (6 - first_day.weekday()) % 7
    # Add the number of days to get the Sunday of that week
    sunday = first_day + timedelta(days=days_to_sunday)
    return sunday

parser = argparse.ArgumentParser()
parser.add_argument("--indicator", help="epidemilogical indicator to be used", default="ILIconsultationrate")
parser.add_argument("--url", help="url to data", 
                    default="https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/ILIARIRates.csv")
parser.add_argument("--pathogen", help="pathogen name", default="SARS-CoV-2")
parser.add_argument("--path_to_save", help="save path")

args = parser.parse_args()
indicator = str(args.indicator)
URL = str(args.url)
pathogen = str(args.pathogen)
path_to_save = str(args.path_to_save)

# import iso2 codes
iso_df = pd.read_csv("../../supporting-files/locations_iso2_codes.csv")

# import erviss data
df = pd.read_csv(URL)

# filter data by pathogen
if URL in ["https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/nonSentinelSeverity.csv"]: 
    df = df.loc[df.pathogen == pathogen]
    df.drop(columns=["pathogen", "pathogentype"], inplace=True)

# format and add info on date, country
df.rename(columns={"countryname": "location_name"}, inplace=True)
df = df.merge(iso_df, on="location_name", how="left")
df["week_end_date"] = df.yearweek.apply(get_sunday_of_week)
df = df.loc[df.indicator == indicator].reset_index(drop=True)
df = df[["survtype", "location_name", "iso2_code", "yearweek", "week_end_date", "indicator", "age", "value"]]


# ILI and ARI for Cyprus, Luxembourg, Malta are per 100
if URL in ["https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/ILIARIRates.csv"]:
    df.loc[df.location_name.isin(["Cyprus", "Malta", "Luxembourg"]), "value"] *= 1000

# save 
df.to_csv(os.path.join(path_to_save, f"{indicator}.csv"), index=False)




