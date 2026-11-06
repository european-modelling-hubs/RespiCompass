# Population data 

The file `population_estimates.csv` contains the number of individuals in different age groups for the EU/EEA countries. It has the following columns: 

| Column Name | Description |
|  :-: |  :-: |
| `country` | Country name |
| `age_group` | Age group (one of: 0-2mo, 3-5mo, 6-11mo, 1-4, 5-17, 18-59, 60-64, 65-69, 70-74, 75-79, 80+) |
| `population` | Number of individuals |

**Note**: this data has to be interpreted as the number of individuals in different age groups in a given country at the beginning of the scenario period.

To load the data in Python, you can use the following code:
```python
import pandas as pd
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/population/population_estimates.csv'
population = pd.read_csv(url)
```

In R, you can use the following code:
```R
library(readr)
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/population/population_estimates.csv'
population <- read_csv(url)
```

## Source and additional information

The number of individuals in different age groups and countries is taken from [Eurostat](https://doi.org/10.2908/DEMO_PJAN). Eurostat provides yearly estimates of usually resident population on January 1st in different European countries at a single year of age resolution (for more details on the definition of usually resident, see [here](https://ec.europa.eu/eurostat/cache/metadata/en/demo_pop_esms.htm#shortdata_descrDisseminated)). We consider the most recent year available in the dataset, which is 2025.

The following age groups are considered to match the requested granularity for this scenario round: 0-2mo, 3-5mo, 6-11mo, 1-4, 5-17, 18-59, 60-64, 65-69, 70-74, 75-79, 80+. Given that there are three groups below 1 year of age, we apply a correction in order to obtain the correct distribution of infants in these subgroups at the beginning of the scenario period. Indeed, due to non-constant birth rates across the months, the distribution of children in these subgroups at any point in time may deviate from the homogeneous case (see [here](../births/) for more details on births data). More in detail, we proceed as follows:

- The total population below 1 year old is set considering the Eurostat data (i.e., 2025 population data).
- The population in each group below 1 year old at the beginning of the scenario (i.e., 2026/09/01) is computed considering the births data from Eurostat, treated as a repeating annual cycle indexed by calendar month:
    - 0-2 mo: born in calendar months June, July, August (0-2 months old on 2026/09/01)
    - 3-5 mo: born in calendar months March, April, May (3-5 months old on 2026/09/01)
    - 6-11 mo: born in calendar months September, October, November, December, January, February (6-11 months old on 2026/09/01)
- Using these estimates of individuals in each subgroup <1 year old, we compute the share of population in each age group below 1 year old at the beginning of the scenario.
- The population below 1 year old at the beginning of the scenario is then distributed in the age groups 0-2mo, 3-5mo, and 6-11mo, considering this share and the total from Eurostat data.

## Contacts
If you have any question regarding this scenario round do not hesitate to get in touch at [rsv-respicompass@isi.it](mailto:rsv-respicompass@isi.it).
