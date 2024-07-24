# Consultation Rate Data

This repository contains datasets related to consultation rates (per 100,000 population) for Acute Respiratory Infections (ARI) and Influenza-like Illnesses (ILI). Each dataset provides detailed information segmented by location, date, and demographic group.
Data are taken from [ERVISS](https://erviss.org/).

## Datasets

### 1. ARIconsultationrate.csv
(Source: [ERVISS](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/ILIARIRates.csv))

This dataset includes information on consultation rates for Acute Respiratory Infections (ARI).

- **Columns:**
  - `survtype`: The type of surveillance (e.g., primary care syndromic).
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `yearweek`: The year and week of the record (e.g., 2024-W21).
  - `week_end_date`: The end date of the week in YYYY-MM-DD format.
  - `indicator`: The type of indicator (e.g., ARIconsultationrate).
  - `age`: The age group (e.g., 0-4, 15-64, total).
  - `value`: The consultation rate (per 100,000 population).

- **Sample Data:**
  ```csv
  survtype,location_name,iso2_code,yearweek,week_end_date,indicator,age,value
  primary care syndromic,Belgium,BE,2024-W21,2024-05-26,ARIconsultationrate,0-4,2157.9
  primary care syndromic,Belgium,BE,2024-W21,2024-05-26,ARIconsultationrate,15-64,748.2
  primary care syndromic,Belgium,BE,2024-W21,2024-05-26,ARIconsultationrate,5-14,979.6
  primary care syndromic,Belgium,BE,2024-W21,2024-05-26,ARIconsultationrate,65+,787.4
  primary care syndromic,Belgium,BE,2024-W21,2024-05-26,ARIconsultationrate,total,854.4
  ```

### 2. ILIconsultationrate.csv
(Source: [ERVISS](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/ILIARIRates.csv))

This dataset includes information on consultation rates for Influenza-like Illnesses (ILI).

- **Columns:**
  - `survtype`: The type of surveillance (e.g., primary care syndromic).
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `yearweek`: The year and week of the record (e.g., 2024-W14).
  - `week_end_date`: The end date of the week in YYYY-MM-DD format.
  - `indicator`: The type of indicator (e.g., ILIconsultationrate).
  - `age`: The age group (e.g., 0-4, 15-64, total).
  - `value`: The consultation rate (per 100,000 population).

- **Sample Data:**
  ```csv
  survtype,location_name,iso2_code,yearweek,week_end_date,indicator,age,value
  primary care syndromic,Austria,AT,2024-W14,2024-04-07,ILIconsultationrate,0-4,0.0
  primary care syndromic,Austria,AT,2024-W14,2024-04-07,ILIconsultationrate,15-64,1802.9
  primary care syndromic,Austria,AT,2024-W14,2024-04-07,ILIconsultationrate,5-14,1944.9
  primary care syndromic,Austria,AT,2024-W14,2024-04-07,ILIconsultationrate,65+,856.9
  primary care syndromic,Austria,AT,2024-W14,2024-04-07,ILIconsultationrate,total,1512.6
  ```

## Usage

These datasets can be used to analyze the trends and patterns in consultation rates over time. The data is structured to allow for time-series analysis and comparison across different locations and demographic groups.

### Example Analysis

To get started with analyzing this data, you can use Python and pandas as follows:

```python
import pandas as pd

# Load datasets
ari_consultation_rate_df = pd.read_csv('ARIconsultationrate.csv')
ili_consultation_rate_df = pd.read_csv('ILIconsultationrate.csv')

# Display the first few rows of each dataset
print(ari_consultation_rate_df.head())
print(ili_consultation_rate_df.head())

# Example: Average ARI consultation rate in a specific week
average_ari_rate_week = ari_consultation_rate_df[ari_consultation_rate_df['yearweek'] == '2024-W21']['value'].mean()
print(f"Average ARI consultation rate in week 2024-W21: {average_ari_rate_week}")

# Example: Total ILI consultation rate in a specific location
total_ili_rate_location = ili_consultation_rate_df[ili_consultation_rate_df['location_name'] == 'Austria']['value'].sum()
print(f"Total ILI consultation rate in Austria: {total_ili_rate_location}")
```

Or, alternatively, in R as follows:
```R
# Load necessary library
library(dplyr)

# Load datasets
ari_consultation_rate_df <- read.csv('ARIconsultationrate.csv')
ili_consultation_rate_df <- read.csv('ILIconsultationrate.csv')

# Display the first few rows of each dataset
head(ari_consultation_rate_df)
head(ili_consultation_rate_df)

# Example: Average ARI consultation rate in a specific week
average_ari_rate_week <- ari_consultation_rate_df %>% 
  filter(yearweek == '2024-W21') %>% 
  summarise(average = mean(value, na.rm = TRUE)) %>% 
  pull(average)
print(paste("Average ARI consultation rate in week 2024-W21:", average_ari_rate_week))

# Example: Total ILI consultation rate in a specific location
total_ili_rate_location <- ili_consultation_rate_df %>% 
  filter(location_name == 'Austria') %>% 
  summarise(total = sum(value, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total ILI consultation rate in Austria:", total_ili_rate_location))
```
