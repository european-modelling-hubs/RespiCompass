# Mortality data

This folder provides two files on all-cause mortality for the EU/EEA countries.

## `mortality_agegroups.csv`

Contains the total number of annual deaths by age group. It has the following columns:

| Column Name | Description |
|  :-: |  :-: |
| `country` | Country name |
| `iso2_code` | ISO-2 country code |
| `age_group` | Age group (one of: `<1`, 1-4, 5-17, 18-59, 60-64, 65-69, 70-74, 75-79, 80+) |
| `reference_year` | Calendar year the death counts refer to (see below) |
| `total_deaths` | Total number of deaths in the given country, age group, and year |

**Note on age groups**: Eurostat only reports deaths at a single-year-of-age resolution below age 1 (a single combined `Y_LT1`, "Less than 1 year", bucket), with no month-level breakdown. This means the finer infant age groups used elsewhere in RespiCompass (0-2mo, 3-5mo, 6-11mo) cannot be derived from this source. Instead, this file reports one combined `<1` age group for all deaths below 1 year of age.

## `mortality_month.csv`

Contains the total number of deaths (all ages, all causes) by month, and the share of the annual total falling in each month. It has the following columns:

| Column Name | Description |
|  :-: |  :-: |
| `country` | Country name |
| `iso2_code` | ISO-2 country code |
| `month` | Calendar month (1-12) |
| `total_deaths` | Total number of deaths in the given country and month |
| `share_of_year` | Share of `reference_year`'s total deaths falling in this month (`total_deaths` in the month divided by the sum of `total_deaths` across all 12 months of `reference_year`) |
| `reference_year` | Calendar year the death counts refer to (see below) |

To load either file in Python, you can use the following code:
```python
import pandas as pd
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/mortality/mortality_agegroups.csv'
mortality_agegroups = pd.read_csv(url)
```

In R, you can use the following code:
```R
library(readr)
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/mortality/mortality_agegroups.csv'
mortality_agegroups <- read_csv(url)
```

## Source and additional information

- `mortality_agegroups.csv` is derived from Eurostat's [Deaths by age and sex](https://ec.europa.eu/eurostat/databrowser/view/demo_magec/default/table?lang=en&category=demo.demo_mor) dataset (dataset DOI: https://doi.org/10.2908/DEMO_MAGEC), which reports annual deaths by single year of age and sex for each country. Single years of age are summed into the age groups listed above. For each country, the **most recent year available** in the dataset is used as `reference_year` (this can differ across countries depending on Eurostat's reporting lag).
- `mortality_month.csv` is derived from Eurostat's [Deaths by month](https://ec.europa.eu/eurostat/databrowser/view/demo_mmonth/default/table?lang=en&category=demo.demo_mor) dataset (dataset DOI: https://doi.org/10.2908/DEMO_MMONTH), which reports total monthly deaths (all ages) for each country. For each country, we select the **most recent year with all 12 months reported** as `reference_year`, so that `share_of_year` is always computed against a complete annual total rather than a partially-reported year (Eurostat's most recent calendar year is typically still incomplete for several countries at the time of extraction).

Both files only include the 30 EU/EEA countries listed in [`supporting-files/countries.csv`](../../supporting-files/countries.csv). Note that Eurostat uses the geo code `EL` for Greece, which is mapped to the ISO-2 code `GR` used throughout RespiCompass.

## Contacts
If you have any question regarding this scenario round do not hesitate to get in touch at [rsv-respicompass@isi.it](mailto:rsv-respicompass@isi.it).
