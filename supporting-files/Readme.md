# Supporting Files

This repository contains supporting files that provide additional information and context for various datasets. These files are intended to complement the main datasets by offering reference data, mappings, and other relevant information.

## Contents

### 1. locations_iso2_codes.csv

This file provides a mapping between the names of various locations (countries) and their corresponding ISO 3166-1 alpha-2 codes.

- **Columns:**
  - `location_name`: The name of the location (country).
  - `iso2_code`: The ISO 3166-1 alpha-2 code of the location.

- **Sample Data:**
  ```csv
  location_name,iso2_code
  Belgium,BE
  Bulgaria,BG
  Czechia,CZ
  Denmark,DK
  Germany,DE
  ```

### 2. iso_weeks.csv

This file provides a list of [ISO weeks](https://en.wikipedia.org/wiki/ISO_week_date) related to Round 1 2024/2025 projections

- **Columns:**
  - `start_week_day`: Start day of the week (Monday).
  - `end_week_day`: End day of the week (Sunday).
  - `year_week`: Year and ISO week in the format YYYY-WW.

- **Sample Data:**
  ```csv
  start_week_day,end_week_day,year_week
  2024-08-05,2024-08-11,2024-32
  2024-08-12,2024-08-18,2024-33
  2024-08-19,2024-08-25,2024-34
  2024-08-26,2024-09-01,2024-35
  2024-09-02,2024-09-08,2024-36
  ```
