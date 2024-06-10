# ILI+ Data

This repository contains data related to Influenza-like Illness surveillance combined with pathogen detection data (ILI+). More in detail, we compute ILI+ signal as follows:

$$ILI+ = ILI \times \frac{Positivity_{Influenza}}{100}$$

Where $Positivity_{Influenza}$ is the test positivity rate for influenza (overall, without considering subtypes) from either sentinel or non-sentinel detections. All countries consider sentinel surveillance except for Malta, Iceland, Croatia, Romania, Latvia, Finland, where non-sentinel detections are considered. Both ILI and detections data are taken from [ERVISS](https://erviss.org/): 
- [ILI consultation rates](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/ILIARIRates.csv)
- [Sentinel detections](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/sentinelTestsDetectionsPositivity.csv)
- [Non-sentinel detections](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/nonSentinelTestsDetections.csv)


## Dataset Overview

The file `ili_plus.csv` in this repository contains weekly ILI+ data across different age groups and locations. Dataset is updated weekly as new data becomes available.

### File: `ili_plus.csv`

| Column Name   | Description                             |
|---------------|-----------------------------------------|
| `location_name` | Name of the location (country)          |
| `iso2_code`   | ISO 3166-1 alpha-2 country code         |
| `yearweek`    | Year and week of the data point (YYYY-WW)|
| `week_end_date`| End date of the week (YYYY-MM-DD)       |
| `age`         | Age group (e.g., 0-4, 15-64, 5-14, 65+, total)|
| `value`       | ILI+ rate per 100,000 population          |
| `source`      | Source of the data (sentinel or non-sentinel)                       |

## Data Sample

Here is a sample of the dataset:

| location_name | iso2_code | yearweek | week_end_date | age   | value      | source  |
|---------------|-----------|----------|---------------|-------|------------|---------|
| Austria       | AT        | 2024-W14 | 2024-04-07    | 0-4   | 0.000000   | sentinel|
| Austria       | AT        | 2024-W14 | 2024-04-07    | 15-64 | 145.060920 | sentinel|
| Austria       | AT        | 2024-W14 | 2024-04-07    | 5-14  | 156.486207 | sentinel|
| Austria       | AT        | 2024-W14 | 2024-04-07    | 65+   | 68.945977  | sentinel|
| Austria       | AT        | 2024-W14 | 2024-04-07    | total | 121.703448 | sentinel|


## Usage

You can load and explore the dataset using Python and pandas:

```python
import pandas as pd

# Load the dataset
ili_plus_df = pd.read_csv('ili_plus.csv')

# Display the first few rows
print(ili_plus_df.head())
```
Or, alternatively, in R

```R
# Load necessary library
library(readr)

# Load the dataset
ili_plus_df <- read_csv('ili_plus.csv')

# Display the first few rows
print(head(ili_plus_df))
```