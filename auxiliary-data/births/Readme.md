# Births data 

The file `births_by_month.csv` contains the number of individuals born in different months for the EU/EEA countries during the scenario period. It has the following columns: 

| Column Name | Description |
|  :-: |  :-: |
| `country` | Name of the country |
| `date` | Date of birth (YYYY-MM-DD). Given that the data is provided at a monthly resolution, the date is the first day of the month (i.e., 2025-09-01 is related to the number of births in September 2025)|
| `month` | Month of birth (this matches the month of the date column, it is provided for convenience) |
| `year` | Year of birth (this matches the year of the date column, it is provided for convenience) |
| `births` | Number of live births in the given month and country |

**Note**: this data has to be interpreted as the number of live births in the given month and country to be used in the scenario period. We leave at the discretion of the modelers to decide how to distribute monthly births to lower time resolution (i.e., weekly or daily).

To load the data in Python, you can use the following code:
```python
import pandas as pd
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/births/births_by_month.csv'
births = pd.read_csv(url)
```

In R, you can use the following code:
```R
library(readr)
url = 'https://raw.githubusercontent.com/european-modelling-hubs/RespiCompass/refs/heads/main/auxiliary-data/births/births_by_month.csv'
births <- read_csv(url)
```

## Source and additional information

Monthly live births in each European country are taken from [Eurostat](https://doi.org/10.2908/DEMO_FMONTH). Eurostat provides historical birth rates in different countries. More in detail, provided monthly births in different countries over the scenario period matches the most recent Eurostat data, which is the period Septmber 2023-April 2024. In this way, different models will consider a common cohort of newborns over the 2025/2026 winter season using most recent data. 