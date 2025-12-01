# European Countries Population Data

This repository contains datasets related to the population distribution across various age groups for 30 European countries. Each file represents data for a specific country, including the total population segmented by age group. Data is taken from [UN World Population Prospects](https://population.un.org/wpp/) (2024 population estimates).

## Datasets

### Sample File: Norway.csv

This dataset includes information on the population distribution for Norway.

- **Columns:**
  - `age_group`: The age group (e.g., 0-4, 5-9, etc.).
  - `population`: The total population in the specified age group.
 
- **Age Groups Covered:**
  - 0-4
  - 5-9
  - 10-14
  - 15-19
  - 20-24
  - 25-29
  - 30-34
  - 35-39
  - 40-44
  - 45-49
  - 50-54
  - 55-59
  - 60-64
  - 65-69
  - 70-74
  - 75-79
  - 80-84
  - 85-89
  - 90-94
  - 95-99
  - 100+

- **Sample Data:**
  ```csv
  age_group,population
  0-4,273874
  5-9,298418
  10-14,322876
  15-19,328313
  20-24,334883
  ```
### Sample File: Norway_aggr.csv

This dataset includes information on the population distribution for Norway for the same age groups used in the epidemiological data. 

- **Columns:**
  - `age_group`: The age group (e.g., 0-4, 5-14, etc.).
  - `population`: The total population in the specified age group.
 
- **Age Groups Covered:**
  - 0-4
  - 5-14
  - 15-64
  - 65+

- **Sample Data:**
  ```csv
  age_group,population
  0-4,273874
  5-14,621294
  15-64,3560689
  65+,1038544
  ```
  
### Files for Other Countries

In the folder, you will find similar CSV files for each of the 30 European countries. Each file follows the same format as described above, providing detailed population data by age group.

## Usage

These datasets can be used to analyze the population distribution across different age groups for European countries. The data is structured to allow for demographic analysis and comparison across different countries.

### Example Analysis

To get started with analyzing this data, you can use Python and pandas as follows:

```python
import pandas as pd

# Load the dataset for Norway
norway_df = pd.read_csv('Norway.csv')

# Display the first few rows of the dataset
print(norway_df.head())

# Example: Total population in Norway
total_population_norway = norway_df['population'].sum()
print(f"Total population in Norway: {total_population_norway}")

# Load the dataset for another country (e.g., Sweden)
sweden_df = pd.read_csv('Sweden.csv')

# Example: Compare total population between Norway and Sweden
total_population_sweden = sweden_df['population'].sum()
print(f"Total population in Sweden: {total_population_sweden}")
```

Or, alternatively, in R as follows:
```R
# Load necessary library
library(dplyr)

# Load the dataset for Norway
norway_df <- read.csv('Norway.csv')

# Display the first few rows of the dataset
head(norway_df)

# Example: Total population in Norway
total_population_norway <- norway_df %>% 
  summarise(total = sum(population, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total population in Norway:", total_population_norway))

# Load the dataset for another country (e.g., Sweden)
sweden_df <- read.csv('Sweden.csv')

# Example: Compare total population between Norway and Sweden
total_population_sweden <- sweden_df %>% 
  summarise(total = sum(population, na.rm = TRUE)) %>% 
  pull(total)
print(paste("Total population in Sweden:", total_population_sweden))
```
