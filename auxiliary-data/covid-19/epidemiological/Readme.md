# COVID-19 Epidemiological Data

This repository contains three datasets related to COVID-19 epidemiological metrics: ICU admissions, hospital admissions, and deaths. Each dataset provides detailed information segmented by location, date, and demographic group.

Data are taken from [ERVISS](https://erviss.org/) 

## Datasets

### 1. ICUadmissions.csv
(Source: [ERVISS](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/nonSentinelSeverity.csv))

This dataset includes information on ICU admissions related to COVID-19.

- **Columns:**
  - `survtype`: The type of surveillance (e.g., non-sentinel).
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `yearweek`: The year and week of the record (e.g., 2023-W19).
  - `week_end_date`: The end date of the week in YYYY-MM-DD format.
  - `indicator`: The type of indicator (e.g., ICUadmissions).
  - `age`: The age group (e.g., 15-64, total).
  - `value`: The number of ICU admissions.

- **Sample Data:**
  ```csv
  survtype,location_name,iso2_code,yearweek,week_end_date,indicator,age,value
  non-sentinel,Austria,AT,2023-W19,2023-05-14,ICUadmissions,15-64,1
  non-sentinel,Austria,AT,2023-W19,2023-05-14,ICUadmissions,total,1
  non-sentinel,Austria,AT,2023-W17,2023-04-30,ICUadmissions,15-64,1
  non-sentinel,Austria,AT,2023-W17,2023-04-30,ICUadmissions,65+,1
  non-sentinel,Austria,AT,2023-W17,2023-04-30,ICUadmissions,total,2
  ```

### 2. hospitaladmissions.csv
(Source: [ERVISS](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/nonSentinelSeverity.csv))

This dataset includes information on hospital admissions related to COVID-19.

- **Columns:**
  - `survtype`: The type of surveillance (e.g., non-sentinel).
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `yearweek`: The year and week of the record (e.g., 2023-W24).
  - `week_end_date`: The end date of the week in YYYY-MM-DD format.
  - `indicator`: The type of indicator (e.g., hospitaladmissions).
  - `age`: The age group (e.g., 15-64, total).
  - `value`: The number of hospital admissions.

- **Sample Data:**
  ```csv
  survtype,location_name,iso2_code,yearweek,week_end_date,indicator,age,value
  non-sentinel,Austria,AT,2023-W24,2023-06-18,hospitaladmissions,15-64,1
  non-sentinel,Austria,AT,2023-W24,2023-06-18,hospitaladmissions,total,1
  non-sentinel,Austria,AT,2023-W23,2023-06-11,hospitaladmissions,15-64,1
  non-sentinel,Austria,AT,2023-W23,2023-06-11,hospitaladmissions,65+,1
  non-sentinel,Austria,AT,2023-W23,2023-06-11,hospitaladmissions,total,2
  ```

### 3. deaths.csv
(Source: [ERVISS](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/nonSentinelSeverity.csv))

This dataset includes information on deaths related to COVID-19.

- **Columns:**
  - `survtype`: The type of surveillance (e.g., non-sentinel).
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `yearweek`: The year and week of the record (e.g., 2023-W25).
  - `week_end_date`: The end date of the week in YYYY-MM-DD format.
  - `indicator`: The type of indicator (e.g., deaths).
  - `age`: The age group (e.g., 0-4, 15-64, total).
  - `value`: The number of deaths.

- **Sample Data:**
  ```csv
  survtype,location_name,iso2_code,yearweek,week_end_date,indicator,age,value
  non-sentinel,Austria,AT,2023-W25,2023-06-25,deaths,0-4,0
  non-sentinel,Austria,AT,2023-W25,2023-06-25,deaths,15-64,2
  non-sentinel,Austria,AT,2023-W25,2023-06-25,deaths,5-14,0
  non-sentinel,Austria,AT,2023-W25,2023-06-25,deaths,65+,3
  non-sentinel,Austria,AT,2023-W25,2023-06-25,deaths,total,5
  ```

## Usage

These datasets can be used to analyze the trends and patterns in COVID-19 healthcare metrics over time. The data is structured to allow for time-series analysis and comparison across different locations and demographic groups.

### Example Analysis

To get started with analyzing this data, you can use Python and pandas as follows:

```python
import pandas as pd

# Load datasets
icu_admissions_df = pd.read_csv('ICUadmissions.csv')
hospital_admissions_df = pd.read_csv('hospitaladmissions.csv')
deaths_df = pd.read_csv('deaths.csv')

# Display the first few rows of each dataset
print(icu_admissions_df.head())
print(hospital_admissions_df.head())
print(deaths_df.head())

# Example: Total ICU admissions in a specific week
total_icu_admissions_week = icu_admissions_df[icu_admissions_df['yearweek'] == '2023-W19']['value'].sum()
print(f"Total ICU admissions in week 2023-W19: {total_icu_admissions_week}")

# Example: Total hospital admissions in a specific location
total_hospital_admissions_location = hospital_admissions_df[hospital_admissions_df['location_name'] == 'Austria']['value'].sum()
print(f"Total hospital admissions in Austria: {total_hospital_admissions_location}")

# Example: Total deaths across all weeks
total_deaths = deaths_df['value'].sum()
print(f"Total deaths: {total_deaths}")
```

Or, alternatively, in R as follows:

```R
# Load necessary library
library(dplyr)

# Load datasets
icu_admissions_df <- read.csv('ICUadmissions.csv')
hospital_admissions_df <- read.csv('hospitaladmissions.csv')
deaths_df <- read.csv('deaths.csv')

# Display the first few rows of each dataset
head(icu_admissions_df)
head(hospital_admissions_df)
head(deaths_df)

# Example: Total ICU admissions in a specific week
total_icu_admissions_week <- icu_admissions_df %>% 
  filter(yearweek == '2023-W19') %>% 
  summarise(total = sum(value, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total ICU admissions in week 2023-W19:", total_icu_admissions_week))

# Example: Total hospital admissions in a specific location
total_hospital_admissions_location <- hospital_admissions_df %>% 
  filter(location_name == 'Austria') %>% 
  summarise(total = sum(value, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total hospital admissions in Austria:", total_hospital_admissions_location))

# Example: Total deaths across all weeks
total_deaths <- deaths_df %>% 
  summarise(total = sum(value, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total deaths:", total_deaths))
```
