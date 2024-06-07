import pandas as pd
import os

def get_country_population(df_total, iso2, year, mult_factor=1000): 
    df_country = df_total.loc[(df_total.Time == year) & \
                              (df_total.ISO2_code == iso2)][["AgeGrp", "PopTotal"]].reset_index(drop=True)
    df_country["PopTotal"] = (df_country.PopTotal * mult_factor).astype(int)
    df_country.rename(columns={"AgeGrp": "age_group", "PopTotal": "population"}, inplace=True)
    return df_country

# import population data from https://population.un.org/wpp/Download/Standard/CSV/
df = pd.read_csv("./WPP2022_Population1JanuaryByAge5GroupSex_Medium.csv", compression="gzip")

# import location isocode
iso_df = pd.read_csv("../../supporting-files/locations_iso2_codes.csv")

# get population for each country 
for _, row in iso_df.iterrows():
    iso2 = row["iso2_code"]
    country = row["location_name"]
    print(f"Processing {country}...")
    df_country = get_country_population(df, iso2, 2024)
    df_country.to_csv(f"../population/{country}.csv", index=False)



