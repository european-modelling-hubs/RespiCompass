# Population data 

The file `population_estimates.csv` contains the number of individuals in different age groups for the EU/EEA countries. It has the following columns: 

| Column Name | Description |
|  :-: |  :-: |
| `country` | Country name |
| `age_group` | Age group (one of: 0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y) |
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

The number of individuals in different age groups and countries is taken from [Eurostat](https://doi.org/10.2908/DEMO_PJAN). Eurostat provides yearly estimates of usually resident population on January $1^{st}$ in different European countries at a single year of age resolution (for more details on the definition of usually resident, see [here](https://ec.europa.eu/eurostat/cache/metadata/en/demo_pop_esms.htm#shortdata_descrDisseminated)). We consider the most recent year available in the dataset that matches the birth data, which is 2023. 

The following age groups are considered to match the requested granularity for this scenario round: 0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y. Given that there are three groups below 1 year of age, we apply a correction in order to obtain the correct distribution of infants in these subgroups at the beginning of the scenario period. Indeed, due to non-constant birth rates across the months, the distribution of children in these subgroups at any point in time may deviate from the homogeneous case (see [here](../births/) for more details on births data). More in detail, we proceed as follows:

- The total population below 1 year old is set considering the Eurostat data (i.e., 2023 population data)
- The population in each group below 1 year old at the beginning of the scenario (i.e., 2025/09/01) is computed considering the births data from Eurostat:
    - 0-2 mo: 0-89 days old (obtained summing all those born between 2023/06/01 (included) and 2023/09/01 (excluded))
    - 3-5 mo: 90-179 days old (obtained summing all those born between 2023/03/01 (included) and 2023/06/01 (excluded))
    - 6-11 mo: 180-364 days old (obtained summing all those born between 2022/09/01 (included) and 2023/03/01 (excluded))
- Using these estimates of individuals in each subgroup <1 year old, we compute the share of population in each age group below 1 year old at the beginning of the scenario.
- The population below 1 year old at the beginning of the scenario is then distributed in the age groups 0-2mo, 3-5mo, and 6-11mo, considering this share and the total from Eurostat data.







