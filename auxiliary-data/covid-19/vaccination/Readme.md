# COVID-19 Vaccination Data

This repository contains three datasets related to COVID-19 vaccination.

## Datasets

### 1. covid_vax_scenarios.csv
This dataset includes vaccination data to be used in the scenarios. 
- **Columns:**
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `scenario`: The scenario to which the data refers to, more in detail:
    - `higher_vax_coverage`: Data related to these rows must be used in scenarios A and B, where we assume a 15% higher vaccine coverage in 60+
    - `lower_vax_coverage`: Data related to these rows must be used in scenarios C and D, where we assume a 15% lower vaccine coverage in 60+
    - `no_vaccination`: Data related to these rows must be used in scenarios E and F, where we assume a no vaccination in all age groups scenario.
  - `target_group`: The demographic group targeted by the vaccination. This is always equal to `60+`, as this is the target group considered in the scenarios definition.
  - `total_doses`: The total number of doses to be administered in the simulation (note that this already accounts for the +/- 15%).
  - `coverage`: The percentage coverage to be used in the simulation (this is simply computed as total_doses / population * 100).
  - `population`: Total 60+ population (used to compute coverage).
 
- **Sample Data:**
  ```csv
  location_name,iso2_code,scenario,target_group,total_doses,coverage,population
  Belgium,BE,higher_vax_coverage,Age60+,1653959,52.6,3141177
  Bulgaria,BG,higher_vax_coverage,Age60+,9517,0.49,1937342
  Cyprus,CY,higher_vax_coverage,Age60+,5422,2.0,265484
  Czechia,CZ,higher_vax_coverage,Age60+,355708,12.7,2787785
  Germany,DE,higher_vax_coverage,Age60+,4395907,17.2,25488000
  ```

**Note**: This dataset includes the total doses administered (or related coverage) for the 60+ age group, which must be used in the simulation to meet the scenario definitions. The implementation of rollout and coverage for other non-target age groups is left to the discretion of the teams. For guidance, please refer to the next two datasets to inform these choices.

### 2. covid_vax_pre23.csv

This dataset includes vaccination data up to the end of 2022.

- **Columns:**
  - `date`: The date of the record in YYYY-MM-DD format.
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `target_group`: The demographic group targeted by the vaccination (e.g., ALL, Age25_49, HCW, LTCF).
  - `dose`: The type of dose administered (e.g., FirstDose, SecondDose).
  - `doses_administered`: The number of doses administered.

- **Sample Data:**
  ```csv
  date,location_name,iso2_code,target_group,dose,doses_administered
  2020-12-20,Denmark,DK,ALL,FirstDose,2
  2020-12-20,Denmark,DK,Age25_49,FirstDose,2
  2020-12-20,Denmark,DK,HCW,FirstDose,0
  2020-12-20,Denmark,DK,LTCF,FirstDose,0
  2020-12-27,Denmark,DK,ALL,FirstDose,9
  ```

### 3. covid_vax_post23.csv

This dataset includes vaccination data from the beginning of 2023 onwards.

- **Columns:**
  - `date`: The date of the record in YYYY-MM-DD format.
  - `location_name`: The name of the location (country or region).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.
  - `target_group`: The demographic group targeted by the vaccination (e.g., ALL).
  - `dose`: The type of dose administered (in this dataset, this column is NaN for all rows).
  - `doses_administered`: The number of doses administered.

- **Sample Data:**
  ```csv
  date,location_name,iso2_code,target_group,dose,doses_administered
  2023-09-30,Belgium,BE,ALL,,431019
  2023-09-30,Bulgaria,BG,ALL,,3455
  2023-09-30,Cyprus,CY,ALL,,1093
  2023-09-30,Czechia,CZ,ALL,,14003
  2023-09-30,Germany,DE,ALL,,201281
  ```

## Usage

These datasets can be used to analyze the trends and patterns in COVID-19 vaccination over time. The data is structured to allow for time-series analysis and comparison across different locations and demographic groups.

### Example Analysis

To get started with analyzing this data, you can use Python and pandas as follows:

```python
import pandas as pd

# Load datasets
pre23_df = pd.read_csv('covid_vax_pre23.csv')
post23_df = pd.read_csv('covid_vax_post23.csv')

# Display the first few rows of each dataset
print(pre23_df.head())
print(post23_df.head())

# Example: Total doses administered in 2022
total_doses_2022 = pre23_df[pre23_df['date'] < '2023-01-01']['doses_administered'].sum()
print(f"Total doses administered in 2022: {total_doses_2022}")

# Example: Total doses administered in 2023
total_doses_2023 = post23_df['doses_administered'].sum()
print(f"Total doses administered in 2023: {total_doses_2023}")
```

Or, alternatively, in R as follows:
```R
# Load necessary library
library(dplyr)

# Load datasets
pre23_df <- read.csv('covid_vax_pre23.csv')
post23_df <- read.csv('covid_vax_post23.csv')

# Display the first few rows of each dataset
head(pre23_df)
head(post23_df)

# Example: Total doses administered in 2022
total_doses_2022 <- pre23_df %>% 
  filter(date < '2023-01-01') %>% 
  summarise(total = sum(doses_administered, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total doses administered in 2022:", total_doses_2022))

# Example: Total doses administered in 2023
total_doses_2023 <- post23_df %>% 
  summarise(total = sum(doses_administered, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total doses administered in 2023:", total_doses_2023))
```
