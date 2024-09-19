## COVID-19 - Round 1 2024/2025 Scenarios
### Deadline
- Submission deadline: 2024/08/31 (after this date a first report for 2024/25 respiratory diseases insights will be drafted with available models' projections)
- Late submissions deadline: 2024/09/20 (draft report will be revised after this date considering all models' projections)

### Rationale
We aim to explore the potential impact of COVID-19 during the upcoming 2024-2025 respiratory disease season. To this end, we have designed a set of scenarios:
1. To anticipate the burden of COVID-19 during the 2024-2025 respiratory disease season under different scenario assumptions
1. To estimate the averted COVID-19 burden due to vaccines in the 2024-2025 season
1. To assess the accuracy of model projections using testable predictions for COVID-19 burden in the EU/EEA and individual countries. This involves understanding the factors that reduce accuracy and identifying ways to improve projections, such as making regional projections and changing modelling targets

### Scenarios
| | **Optimistic vaccine-induced immunity waning** (Protection against infection: 6 months median time to transition to 50% of the initial immunity; Protection against severe outcomes, e.g., hospitalisation: no waning) | Pessimistic vaccine-induced immunity waning (Protection against infection: 6 months median time to transition to 30% of the initial immunity; Protection against severe outcomes, e.g., hospitalisation: 6 months median time to transition to 60% of the initial immunity) |
|  :-:|  :-: | :-: |
| **Higher than usual Vaccine Coverage** (Vaccine coverage is 15% higher than in the 2023-24 winter season in 60+ in all countries) | Scenario A | Scenario B |
| **Lower than usual Vaccine Coverage** (Vaccine coverage is 15% lower than in the 2023-24 winter season in 60+ in all countries) | Scenario C | Scenario D |
| **No Vaccination** (baseline scenario without vaccination) | Scenario E | Scenario F |


### Targets
We are currently asking for weekly COVID-19 hospital admissions (mandatory) and infections (optional) between August 5, 2024 and June 1, 2025 in European countries by age groups (0-4, 5-14, 15-64, 65+, total) and vaccination status (yes, no). **Note**: here “vaccinated” indicates individuals that received a vaccination during the 2024/2025 season.

The list of countries is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/locations_iso2_codes.csv) and the list of weeks is provided [here]([TODO](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/iso_weeks.csv)). Historical hospital admissions data is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/covid-19/hospitaladmissions.csv).

### Submission Format
General guidance for the submission format is provided in the [Wiki](https://github.com/european-modelling-hubs/RespiCompass/wiki/Submission-format). For this specific COVID-19 round, submission file must be named

```2024_2025_1_COVID-<team>-<model>.parquet```

Where `<team>-<model>` will be specific for each team/model and must match the team_abbr and model_abbr parameters in the metadata file. Additionally, you should set: 
-  ```round_id = '2024_2025_1_COVID'```
-  ```scenario_id```: allowed values are ```'A', 'B', 'C', 'D', 'E', 'F'``` related to different scenarios
-  ```target = 'hospital_admissions'``` or ```target = 'infections'```
-  ```pop_group``` allowed values are ```'0-4_vaxYes', '0-4_vaxNo', '0-4_vaxTotal', '5-14_vaxYes', '5-14_vaxNo', '5-14_vaxTotal', '15-64_vaxYes', '15-64_vaxNo', '15-64_vaxTotal', '65+_vaxYes', '65+_vaxNo', '65+_vaxTotal', 'total_vaxYes', 'total_vaxNo', 'total_vaxTotal'```, covering all combinations of considered age groups and vaccination status. Note that groups ```vaxYes``` are individuals that received an updated annual boosters during the 2024-2025 season
- ```horizon```: weeks ahead in the projection period, see this [file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/iso_weeks.csv) for a horizon/week correspondence
- ```target_end_date``` end date of target week, see this [file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/iso_weeks.csv) for a date/week correspondence
- ```output_type```: we request teams to submit 100-300 individual trajectories for each scenario (at least 100 are needed, at most 300 are accepted). For trajectories ```output_type='sample'```. Teams may also submit quantiles, but this optional. In that case ```output_type='quantile'```
- ```output_type_id```: '1' to '300' for samples, one of the allowed quantiles for quantile output type

### Shared Assumptions
#### COVID-19 Waning Immunity
We assume that vaccine-induced immunity wanes at specific rates as outlined in the scenario axes. In Scenario A, C, E, we assume a median time of 6 months for immunity to decline to 50% of the initial vaccine effectiveness (VE). This means that an individual vaccinated against COVID-19 on day t with a certain VE will, after 6 months (in median terms), have a protection level of 0.5 x VE against infection. In these scenarios, we also assume that VE against severe outcomes, such as hospitalisation, does not wane. In scenarios B, D, F, we assume that after 6 months, the VE against infection will decrease to 0.3 of the initial VE, and VE against hospitalisation will decrease to 0.6 of the initial VE. In this round, waning immunity reflects both the decline of immune system responses over time and the gradual immune escape of the virus.

We acknowledge that VE may continue to wane beyond the 6-month median time, leaving the specifics of this progression to the discretion of the modellers. Additionally, modellers have the flexibility to determine the method of waning implementation (e.g., linear decay of immunity, stepwise approach, etc). 

We note that the scenario assumptions pertain specifically to the waning of vaccine-induced immunity. Modellers should also incorporate the waning of natural immunity; however, the rate of waning for natural immunity must be slower than that of vaccine-induced immunity.

Additionally, for this round, teams should not factor in the additional impact of reduced protection due to the emergence of immune escape variants. Although we are not explicitly modelling the emergence of immune-escaping variants in this round, this factor is effectively accounted for in the waning of immunity.

Waning immunity estimates from studies considered to define scenario assumptions are reported [here](https://docs.google.com/document/d/1MthtD6EWm4UWsjJttNUKYHP-O9oLqSv2vAXL-1aHXFA/edit?usp=sharing).

#### COVID-19 Vaccine Effectiveness
For all scenarios we assume a VE against infection of 50% few days after inoculation in line with recent studies. We assume a VE against hospitalisation few days after inoculation of 75%, compatible with recent studies. Importantly, this VE reflects the combined effects of protection against both infection and hospitalisation in the event of a breakthrough infection. For this round we assume the same VE for all age groups.
Teams may, at their discretion, include additional effects of vaccines, such as the reduced infectiousness of vaccinated individuals if they become infected.

VE estimates from studies considered to define scenario assumptions are reported [here](https://docs.google.com/document/d/1XdbVyWbehuqqa2qdu7028tWh7UGCSP2V-opsp4F83fo/edit?usp=sharing).

#### Vaccine Coverage
In scenarios A and B, we assume vaccination coverage for the 60+ age group is 15% higher compared to the data reported during the 2023/2024 winter season. This represents a relative increase, meaning that a coverage of 50% would increase to 57.5%.

In scenarios C and D, we assume vaccination coverage for the 60+ age group is 15% lower compared to the data reported during the 2023/2024 winter season.

Teams should maintain vaccination coverage in other age groups at the same levels as the 2023/2024 winter season. If data on vaccination coverage in other age groups are not available, teams can make assumptions, provided the coverage remains lower than that of the 60+ (at-risk) population.

Scenarios E and F are hypothetical scenarios where teams are asked not to include vaccinations in any age groups. These scenarios are used to estimate the effect of vaccinations against a baseline scenario in which they are completely absent.

We leave the implementation of the vaccination rollout to the discretion of the teams. This includes decisions on whether to use constant or time-varying administration rates and whether to administer most doses before the respiratory disease season. We leave it to the modeller’s discretion how specific population groups (e.g., individuals with comorbidities, health care workers) are vaccinated in their model.

Doses administered (and related vaccine coverage) for the 60+ age group, already adjusted according to the scenario definitions, are provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/vaccination/covid_vax_scenarios.csv).


### Data
We provide the following data to support models development and calibration.

Target data: 
- [historical hospital admissions](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/covid-19/hospitaladmissions.csv) data by age group and country

Vaccination data: 
- [Scenario vaccination coverage](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/vaccination/covid_vax_scenarios.csv): vaccine coverage data for the 60+ age group to be used in the scenarios (i.e., already adjusted according to the scenario definitions) 

Auxiliary data: 
- COVID-19 [ICU](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/epidemiological/ICUadmissions.csv) admissions and [deaths](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/epidemiological/deaths.csv) 
- [Vaccination after 2023](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/vaccination/covid_vax_post23.csv) (needed for scenario axis, more information above) and [before 2023](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/covid-19/vaccination/covid_vax_pre23.csv)
- [Pathogen detections](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/miscellaneous/detections/pathogen_detection.csv)
- [Population](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/miscellaneous/population) by age group in different European countries

Additional references to external data sources that may be used for modeling are provided [here](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data)


