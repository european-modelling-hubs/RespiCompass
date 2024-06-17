## Influenza - Round 1 2024/2025 Scenarios
Deadline: 
- First deadline: 2024/08/31 (after this date a first report for 2024/25 respiratory diseases insights will be drafted with available models' projections)
- Second deadline: 2024/09/30 (draft report will be revised after this date considering all models' projections)

| | Lower Burden Season (Transmission potential* is 10% lower with respect to last three influenza seasons, excluding pandemic years) | Higher Burden Season (Transmission potential is 10% higher with respect to last three influenza seasons, excluding pandemic years) |
|  :-:|  :-: | :-: |
| Higher than usual Vaccine Coverage (Vaccine coverage is 15% higher than last flu season with available data in 65+ in all countries) | Scenario A | Scenario B |
| Lower than usual Vaccine Coverage (Vaccine coverage is 15% lower than last flu season with available data in 65+ in all countries) | Scenario C | Scenario D |
| No Vaccination (baseline scenario without vaccination) | Scenario E | Scenario F |

### Shared Assumptions
#### Vaccine Effectiveness

#### Vaccine Rollout


### Targets and Submission Format
We are currently asking for ILI+ weekly between August 1, 2024 and May 31, 2025 in European countries for the following age groups: 0-4, 5-14, 15-64, 65+, total.

The list of countries is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/locations_iso2_codes.csv) and the list of weeks is provided [here](TODO). ILI+ is computed as follows:

$$ILI+ = ILI \times \frac{Positivity_{Influenza}}{100}$$

Where ILI is the consulation rate for influenza-like-illness reported in a given country and week, and $Positivity_{Influenza}$ is the test positivity rate for influenza (overall, without considering subtypes) from either sentinel or non-sentinel detections in that country and week. All countries consider sentinel surveillance except for Malta, Iceland, Croatia, Romania, Latvia, Finland, where non-sentinel detections are considered. Historical ILI+ data is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/influenza/ili_plus.csv).

### Data
We provide the following data to support models development and calibration.

Target data: 
- [historical ILI+](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/influenza/ili_plus.csv) data by age group and country

Auxiliary data: 
- [ILI](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/epidemiological/ILIconsultationrate.csv) and [ARI](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/epidemiological/ARIconsultationrate.csv) consultation rates
- [Vaccination for 65+](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/vaccination/vaccine_coverage_65plus.csv) (needed for scenario axis, more information above) and for all [other available age groups](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/vaccination/vaccine_coverage_all.csv)
- [Pathogen detections](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/miscellaneous/detections/pathogen_detection.csv)
- [Population](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/miscellaneous/population) by age group in different European countries

Additional references to external data sources that may be used for modeling are provided [here](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data)

