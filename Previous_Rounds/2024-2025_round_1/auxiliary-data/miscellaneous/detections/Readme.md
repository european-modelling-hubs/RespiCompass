# Pathogen Detections Data

This folder contains pathogen detection. The dataset includes information about sentinel and non-sentinel detections of Influenza (and subtypes), SARS-CoV-2, and RSV, includeing the number of detections and tests conducted across different locations and time periods. Data are taken from [ERVISS](https://erviss.org/): 
- [Sentinel detections](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/sentinelTestsDetectionsPositivity.csv)
- [Non-sentinel detections](https://github.com/EU-ECDC/Respiratory_viruses_weekly_data/blob/main/data/nonSentinelTestsDetections.csv)


## Dataset

The dataset provided in the `pathogen_detection.csv` file includes the following columns:

- `survtype`: The type of surveillance (sentinel or non-sentinel).
- `location_name`: The name of the location where data was collected.
- `iso2_code`: The ISO 3166-1 alpha-2 code of the country.
- `yearweek`: The year and week of the data collection.
- `week_end_date`: The ending date of the week for the data collection.
- `pathogen`: The name of the pathogen (e.g., Influenza, RSV).
- `pathogentype`: The type of the pathogen.
- `pathogensubtype`: The subtype of the pathogen.
- `indicator`: The type of measurement (e.g., detections, tests).
- `age`: The age group of the subjects (e.g., total).
- `value`: The value of the measurement (e.g., number of detections or tests).


## Usage

### Example Script

```python
import pandas as pd

# Load the dataset
data = pd.read_csv('test.csv')

# Display the first few rows of the dataset
print(data.head())

# Perform your analysis here
```

Or, alternatively, in R: 
```R
# Load the necessary library
library(readr)

# Load the dataset
data <- read_csv('test.csv')

# Display the first few rows of the dataset
print(head(data))

# Perform your analysis here
```
