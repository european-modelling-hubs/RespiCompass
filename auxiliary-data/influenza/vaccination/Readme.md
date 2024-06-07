# Influenza Vaccine Coverage Data

This repository contains datasets related to Influenza vaccine coverage. The datasets provide information on vaccine coverage for all age groups and specifically for individuals aged 65 and above.

## Datasets

### 1. vaccine_coverage_all.csv

This dataset includes information on vaccine coverage for all age groups.

- **Columns:**
  - `season`: The vaccination season (e.g., 2020-2021).
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `target_group`: The demographic group targeted by the vaccination (e.g., 65+y for individuals aged 65 and above).
  - `vaccine_coverage`: The percentage of the population covered by the vaccine.
  - `source`: The source of the data (e.g., EUROSTAT).

- **Sample Data:**
  ```csv
  season,location_name,iso2_code,target_group,vaccine_coverage,source
  2020-2021,Belgium,BE,65+y,57.33,EUROSTAT
  2019-2020,Belgium,BE,65+y,62.06,EUROSTAT
  2018-2019,Belgium,BE,65+y,55.1,EUROSTAT
  2017-2018,Belgium,BE,65+y,53.19,EUROSTAT
  2016-2017,Belgium,BE,65+y,52.88,EUROSTAT
  ```

### 2. vaccine_coverage_65plus.csv

This dataset includes information on vaccine coverage specifically for individuals aged 65 and above.

- **Columns:**
  - `season`: The vaccination season (e.g., 2020-2021).
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `target_group`: The demographic group targeted by the vaccination (e.g., 65+y for individuals aged 65 and above).
  - `vaccine_coverage`: The percentage of the population covered by the vaccine.
  - `source`: The source of the data (e.g., EUROSTAT).
  - `is_reference`: Indicates if the data is a reference value (True or False).

- **Sample Data:**
  ```csv
  season,location_name,iso2_code,target_group,vaccine_coverage,source,is_reference
  2020-2021,Belgium,BE,65+y,57.33,EUROSTAT,True
  2019-2020,Belgium,BE,65+y,62.06,EUROSTAT,False
  2018-2019,Belgium,BE,65+y,55.1,EUROSTAT,False
  2017-2018,Belgium,BE,65+y,53.19,EUROSTAT,False
  2016-2017,Belgium,BE,65+y,52.88,EUROSTAT,False
  ```

## Usage

These datasets can be used to analyze the trends and patterns in Influenza vaccine coverage over time. The data is structured to allow for time-series analysis and comparison across different locations and demographic groups.

### Example Analysis

To get started with analyzing this data, you can use Python and pandas as follows:

```python
import pandas as pd

# Load datasets
vaccine_coverage_all_df = pd.read_csv('vaccine_coverage_all.csv')
vaccine_coverage_65plus_df = pd.read_csv('vaccine_coverage_65plus.csv')

# Display the first few rows of each dataset
print(vaccine_coverage_all_df.head())
print(vaccine_coverage_65plus_df.head())

# Example: Average vaccine coverage for all age groups in the 2020-2021 season
average_coverage_all_2020 = vaccine_coverage_all_df[vaccine_coverage_all_df['season'] == '2020-2021']['vaccine_coverage'].mean()
print(f"Average vaccine coverage for all age groups in the 2020-2021 season: {average_coverage_all_2020}")

# Example: Average vaccine coverage for 65+ age group in the 2020-2021 season
average_coverage_65plus_2020 = vaccine_coverage_65plus_df[vaccine_coverage_65plus_df['season'] == '2020-2021']['vaccine_coverage'].mean()
print(f"Average vaccine coverage for 65+ age group in the 2020-2021 season: {average_coverage_65plus_2020}")
```

Or, alternatively, in R as follows:
```R
# Load necessary library
library(dplyr)

# Load datasets
vaccine_coverage_all_df <- read.csv('vaccine_coverage_all.csv')
vaccine_coverage_65plus_df <- read.csv('vaccine_coverage_65plus.csv')

# Display the first few rows of each dataset
head(vaccine_coverage_all_df)
head(vaccine_coverage_65plus_df)

# Example: Average vaccine coverage for all age groups in the 2020-2021 season
average_coverage_all_2020 <- vaccine_coverage_all_df %>% 
  filter(season == '2020-2021') %>% 
  summarise(average = mean(vaccine_coverage, na.rm = TRUE)) %>% 
  pull(average)
print(paste("Average vaccine coverage for all age groups in the 2020-2021 season:", average_coverage_all_2020))

# Example: Average vaccine coverage for 65+ age group in the 2020-2021 season
average_coverage_65plus_2020 <- vaccine_coverage_65plus_df %>% 
  filter(season == '2020-2021') %>% 
  summarise(average = mean(vaccine_coverage, na.rm = TRUE)) %>% 
  pull(average)
print(paste("Average vaccine coverage for 65+ age group in the 2020-2021 season:", average_coverage_65plus_2020))
```
