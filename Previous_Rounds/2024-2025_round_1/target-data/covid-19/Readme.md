# Hospital Admission Data

This repository contains data of COVID-19 related hospital admissions. Data are taken from [ERVISS](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/nonSentinelSeverity.csv).


## Dataset Overview

The file `hospitaladmissions.csv` in this repository contains weekly COVID-19 related hospital admissions data across different age groups and locations. Dataset is updated weekly as new data becomes available.

### File: `hospitaladmissions.csv`

| Column Name   | Description                             |
|---------------|-----------------------------------------|
| `survtype` | The type of surveillance (e.g., non-sentinel)          |
| `location_name`   |  The name of the location (country or region).        |
| `iso2_code`    | The ISO 3166-1 alpha-2 code of the location. |
| `yearweek`|     The year and week of the record (e.g., 2023-W24).    |
| `week_end_date`         |  The end date of the week in YYYY-MM-DD format.|
| `indicator`       |  The type of indicator (e.g., hospitaladmissions).   |
| `age`      |  The age group (e.g., 15-64, total). |
| `value`      |    The number of hospital admissions.               |

## Data Sample

Here is a sample of the dataset:
| survtype     | location_name | iso2_code | yearweek | week_end_date | indicator          | age  | value |
|--------------|---------------|-----------|----------|---------------|--------------------|------|-------|
| non-sentinel | Austria       | AT        | 2023-W24 | 2023-06-18    | hospitaladmissions | 15-64| 1     |
| non-sentinel | Austria       | AT        | 2023-W24 | 2023-06-18    | hospitaladmissions | total| 1     |
| non-sentinel | Austria       | AT        | 2023-W23 | 2023-06-11    | hospitaladmissions | 15-64| 1     |
| non-sentinel | Austria       | AT        | 2023-W23 | 2023-06-11    | hospitaladmissions | 65+  | 1     |
| non-sentinel | Austria       | AT        | 2023-W23 | 2023-06-11    | hospitaladmissions | total| 2     |


## Usage

You can load and explore the dataset using Python and pandas:

```python
import pandas as pd

# Load the dataset
hospitaladmissions_df = pd.read_csv('hospitaladmissions.csv')

# Display the first few rows
print(hospitaladmissions_df.head())
```
Or, alternatively, in R

```R
# Load necessary library
library(readr)

# Load the dataset
hospitaladmissions_df <- read_csv('hospitaladmissions.csv')

# Display the first few rows
print(head(hospitaladmissions_df))
```
