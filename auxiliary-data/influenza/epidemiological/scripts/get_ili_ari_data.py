import pandas as pd 
from datetime import datetime, timedelta
import argparse 

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

args = parser.parse_args()
indicator = str(args.indicator)
iso_df = pd.read_csv("../../../../supporting-files/locations_iso2_codes.csv")

# import ILI/ARI data
df = pd.read_csv("https://raw.githubusercontent.com/EU-ECDC/Respiratory_viruses_weekly_data/main/data/ILIARIRates.csv")

# format and add info on date, country
df.rename(columns={"countryname": "location_name"}, inplace=True)
df = df.merge(iso_df, on="location_name", how="left")
df["week_end_date"] = df.yearweek.apply(get_sunday_of_week)
df = df.loc[df.indicator == indicator].reset_index(drop=True)
df = df[["survtype", "location_name", "iso2_code", "yearweek", "week_end_date", "indicator", "age", "value"]]

# Cyprus, Luxembourg, Malta are per 100
df.loc[df.location_name.isin(["Cyprus", "Malta", "Luxembourg"]), "value"] *= 1000

# save 
df.to_csv(f"../{indicator}.csv", index=False)




