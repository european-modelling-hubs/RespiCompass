# Supporting Files

This repository contains the following additional supporting files: 

1. `countries.csv`: This file provides a mapping between the names of various countries and their corresponding [ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). **Columns:**
    - `country`: The name of the country.
    - `iso2_code`: The ISO 3166-1 alpha-2 code of the country.

2. `isoweeks.csv`: 
This file provides a list of [ISO weeks](https://en.wikipedia.org/wiki/ISO_week_date) related to the scenario period of RSV scenario round 2025/2026. **Columns:**
    - `target_start_date`: Start day of the week (Monday).
    - `target_end_date`: End day of the week (Sunday).
    - `week`: Week number.
    - `year`: Year.
    - `year_week`: Year and ISO week in the format ```YYYY-Www```.
    - `horizon`: Weeks ahead in the projection period. Weeks ahead are defined relative to the start of the projection: week $0$ corresponds to the first week of the projection period starting on September $1^{st}$, 2025, while negative values represent prior weeks. These past weeks are included because, in the case of maternal vaccination scenarios (C and D), teams are expected to report doses administered before September $1^{st}$, 2025, as the first immunized infants should be born on that date.
  

# Contacts
If you have any question regarding this scenario round do not hesitate to get in touch at [rsv-respicompass@isi.it](mailto:rsv-respicompass@isi.it).
