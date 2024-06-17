# RespiCompass - European Respiratory Diseases Scenario Hub

## Rationale 
TODO

## How to Join RespiCompass
RespiCompass welcomes teams willing to contribute their projections. Detailed information on how to join are provided in the [Wiki](link). Here’s a concise guide on how to participate:

1. **Create a Metadata File**:
   - Include key information about your team and model.
   - Detailed instructions can be found [here](link).

2. **Develop Your Model**:
   - Independently develop your model and produce projections.
   - Ensure your projections respect the provided scenario assumptions (see below).

3. **Submit Model Projections**:
   - Follow the submission format detailed [here](link).
   - Submit your projections via a pull request as outlined [here](link).

For any questions, please email us at [modelling@ecdc.europa.eu](mailto:modelling@ecdc.europa.eu).

You can choose to participate in projections for either COVID-19 or Influenza, and for a single or a limited number of countries.


## COVID-19 - Round 1 2024/2025 Scenarios
Deadline: 
- First deadline: 2024/08/31 (after this date a first report for 2024/25 respiratory diseases insights will be drafted with available models' projections)
- Second deadline: 2024/09/30 (draft report will be revised after this date considering all models' projections)

| | Optimistic waning (Protection against infection: 6 months median time to transition to 70% of the initial immunity; Protection against severe outcomes: no waning) | Pessimistic waning (Protection against infection: 6 months median time to transition to 40% of the initial immunity; Protection against severe outcomes: 6 months median time to transition to 80% of the initial immunity) |
|  :-:|  :-: | :-: |
| Higher than usual Vaccine Coverage (Vaccine coverage is 15% higher than in the 2023-24 winter season in 65+ in all countries) | Scenario A | Scenario B |
| Lower than usual Vaccine Coverage (Vaccine coverage is 15% lower than in the 2023-24 winter season in 65+ in all countries) | Scenario C | Scenario D |
| No Vaccination (baseline scenario without vaccination) | Scenario E | Scenario F |

### Shared Assumptions
TODO

### Targets and Submission Format
We are currently asking for weekly hospital admissions related to COVID-19 between August 1, 2024 and May 31, 2025 in European countries for the following age: 0-4, 5-14, 15-64, 65+, total.

The list of countries is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/locations_iso2_codes.csv) and the list of weeks is provided [here](TODO). Historical hospital admissions data is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/covid-19/hospitaladmissions.csv).

### Data
We provide the following data to support models development and calibration.

Target data: 
- [historical hospital admissions](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/covid-19/hospitaladmissions.csv) data by age group and country

Auxiliary data: 
- COVID-19 [ICU](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/epidemiological/ICUadmissions.csv) admissions and [deaths](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/epidemiological/deaths.csv) 
- [Vaccination after 2023](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/vaccination/covid_vax_post23.csv) (needed for scenario axis, more information above) and [before 2023](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/vaccination/covid_vax_pre23.csv)
- [Pathogen detections](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/miscellaneous/detections/pathogen_detection.csv)
- [Population](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/miscellaneous/population) by age group in different European countries

Additional references to external data sources that may be used for modeling are provided [here](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data)


