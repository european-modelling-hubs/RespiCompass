# Births data 

The file `births.csv` contains the number of individuals born in different months for the EU/EEA countries during the scenario period. It has the following columns: 

| Column Name | Description |
|  :-: |  :-: |
| `country` | Country code (ISO 3166-1 alpha-2) |
| `date` | Date of birth (YYYY-MM-DD). Given that the data is provided at a monthly resolution, the date is the first day of the month (i.e., 2025-09-01 is related to the number of births in September 2025)|
| `births` | Number of live births in the given month and country |

**Note**: this data has to be interpreted as the number of live births in the given month and country to be used in the scenario period. We leave at the discretion of the modelers to decide how to distribute monthly births to lower time resolution (i.e., weekly or daily).

To load the data in Python, you can use the following code:
```python
import pandas as pd
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/births/births.csv'
births = pd.read_csv(url)
```

In R, you can use the following code:
```R
library(readr)
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/births/births.csv'
births <- read_csv(url)
```

## Source and additional information

Monthly live births in each European country are taken from [Eurostat](https://doi.org/10.2908/DEMO_FMONTH). Eurostat provides historical birth rates in different countries. More in detail, we will provide modeling teams with monthly births in different countries over the whole scenario period by considering the most recent Eurostat data, which is the period XXXX-XXXX. In this way, different models will consider a common cohort of newborns over the 2025/2026 winter season. 