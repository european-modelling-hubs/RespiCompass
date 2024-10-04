## Influenza - Round 1 2024/2025 Scenarios
### Deadline
- Submission deadline: 2024/08/31 (after this date a first report for 2024/25 respiratory diseases insights will be drafted with available models' projections)
- Late submissions deadline: 2024/09/20 (draft report will be revised after this date considering all models' projections)

### Rationale and Goals
We aim to explore the potential impact of Influenza during the upcoming 2024-2025 respiratory disease season. To this end, we have designed a set of scenarios: 
1. To anticipate the burden of Influenza during the 2024-2025 respiratory disease season under different scenario assumptions
1. To estimate the averted Influenza burden due to vaccines in the 2024-2025 season
1. To assess the accuracy of model projections using testable predictions for Influenza burden in the EU/EEA and individual countries. This involves understanding the factors that reduce accuracy and identifying ways to improve projections, such as making regional projections and changing modelling targets
 
### Scenarios
| | Typical Burden Season (Transmission potential* is equal to average of last three influenza seasons (excluding pandemic years) | Higher Burden Season (Transmission potential is 10% higher with respect to average of last three influenza seasons, excluding pandemic years) |
|  :-:|  :-: | :-: |
| **Higher than usual Vaccine Coverage** (Vaccine coverage is 15% higher than last flu season with available data in 65+ age group in all countries) | Scenario A | Scenario B |
| **Lower than usual Vaccine Coverage** (Vaccine coverage is 15% lower than last flu season with available data in 65+ age group in all countries) | Scenario C | Scenario D |
| **No Vaccination** (baseline scenario without vaccination) | Scenario E | Scenario F |

*Teams should use data from the last three influenza seasons (2017-2018, 2018-2019, and 2023-2024 excluding pandemic years) to estimate an average transmission potential (e.g., $R_t$) and assume it to be equal or 10% higher depending on the scenario. Transmission potential includes all factors that may impact transmission rate, except for vaccination coverage, which is captured by the other scenario axis. 

**Note**: The scenario definitions for Influenza have been updated from the initial formulation. Originally, they included a lower and higher burden season, but now they reflect a typical and higher burden season.

### Targets
We are currently asking for ILI+ weekly incidence between August 5, 2024 and June 1, 2025 in European countries by age groups (0-4, 5-14, 15-64, 65+, total) and vaccination status (yes, no, total). Note: here “vaccinated” indicates individuals that received a vaccination during the 2024/2025 season, while "not vaccinated" are those that did not received a vaccination during the 2024/2025 season. The total vaccination group is the sum of those vaccinated and not vaccianted during the 2024/2025 season. 

The list of countries is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/locations_iso2_codes.csv) and the list of weeks is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/iso_weeks.csv). ILI+ is computed as follows:

$$ILI+ = ILI \times \frac{Positivity_{Influenza}}{100}$$

Where ILI is the consulation rate for influenza-like-illness reported in a given country and week, and $Positivity_{Influenza}$ is the test positivity rate for influenza (overall, without considering subtypes) from either sentinel or non-sentinel detections in that country and week. All countries consider sentinel surveillance except for Malta, Iceland, Croatia, Romania, Latvia, Finland, where non-sentinel detections are considered. Historical ILI+ data is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/influenza/ili_plus.csv). The rationale for using ILI+ instead of ILI is rooted in the increased non-specificity of ILI, particularly after the advent of COVID-19. By combining ILI with detection rates, we obtain a signal more specific to influenza (see [here for past seasons ILI+ and ILI curves](https://docs.google.com/presentation/d/1uvEMVCRCTCAU0ehESodntArCBK9Gel8yZXVYshVs6yY/edit?usp=sharing)).

### Submission Format
General guidance for the submission format is provided in the [Wiki](https://github.com/european-modelling-hubs/RespiCompass/wiki/Submission-format). For this specific Influenza round, submission file must be saved in [parquet format](https://parquet.apache.org/) and named

```2024_2025_1_FLU-<team>-<model>.parquet```

Where `<team>-<model>` will be specific for each team/model and must match the team_abbr and model_abbr parameters in the metadata file. Additionally, you should set: 
-  ```round_id = '2024_2025_1_FLU'```
-  ```scenario_id```: allowed values are ```'A', 'B', 'C', 'D', 'E', 'F'``` related to different scenarios
-  ```target = 'ili_plus'```
-  ```pop_group``` allowed values are ```'0-4_vaxYes', '0-4_vaxNo', '0-4_vaxTotal', '5-14_vaxYes', '5-14_vaxNo', '5-14_vaxTotal', '15-64_vaxYes', '15-64_vaxNo', '15-64_vaxTotal', '65+_vaxYes', '65+_vaxNo', '65+_vaxTotal', 'total_vaxYes', 'total_vaxNo', 'total_vaxTotal'```,, covering all combinations of considered age groups and vaccination status. Note that groups ```vaxYes``` are individuals that received an updated annual vaccination during the 2024-2025 season
- ```horizon```: weeks ahead in the projection period, see this [file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/iso_weeks.csv) for a horizon/week correspondence
- ```target_end_date``` end date of target week, see this [file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/iso_weeks.csv) for a date/week correspondence
- ```output_type```: we request teams to submit 100-300 individual trajectories for each scenario (at least 100 are needed, at most 300 are accepted). For trajectories ```output_type='sample'```. Teams may also submit quantiles, but this optional. In that case ```output_type='quantile'```
- ```output_type_id```: '1' to '300' for samples, one of the allowed quantiles for quantile output type

### Shared Assumptions
List of shared assumptions
- Vaccination coverage in 65+ age group as outlined in the scenario axes
- Teams should maintain vaccination coverage in other age groups at the same levels as the 2023/2024 winter season
- VE against laboratory confirmed ILI case of 40% few days after inoculation
- There is sufficient vaccine supply.
- No new public health and social measures (non-pharmaceutical interventions / NPIs).
- No changes in demography given the short timeframe.

Below we provide more details on specific shared assumptions.

#### Vaccine Effectiveness (VE)
For all scenarios we assume a VE = 40% against symptomatic infection based on available literature (see [here](https://docs.google.com/document/d/1RKkT9aYD5D8tsRYE1-jQ1jUDhckEWxIhMQ9plO1dk_c/edit?usp=sharing) for list of studies considered). For this round we assume the same VE for all age groups.
Teams may, at their discretion, include additional effects of vaccines, such as the reduced infectiousness of vaccinated individuals if they become infected. Teams can model waning of vaccine-induced protection at their discretion. It is important to note that these VE estimates are based on individuals who received an updated vaccine in the studied season, compared to those who did not. Therefore, the VE is not being assessed against a completely naive population.

#### Vaccine Coverage and Rollout
In scenarios A and B, we assume vaccination coverage for the 65+ age group is 15% higher compared to the data reported during the last season for which data is available (2021/2022 for most of the countries). This represents a relative increase, meaning that a coverage of 50% would increase to 57.5%.

In scenarios C and D, we assume vaccination coverage for the 65+ age group is 15% lower compared to the data reported during the last season for which data is available

Teams should maintain vaccination coverage in other age groups at the same levels as the last season for which data is available. If data on vaccination coverage in other age groups are not available, teams can make assumptions, provided the coverage remains lower than that of the 65+ age group (at-risk) population.

Scenarios E and F are hypothetical scenarios where teams are asked not to include vaccinations in any age groups. These scenarios are used to estimate the effect of vaccinations against a baseline scenario in which they are completely absent.

We leave the implementation of the vaccination rollout to the discretion of the teams. This includes decisions on whether to use constant or time-varying administration rates and whether to administer most doses before the respiratory disease season.

Vaccine coverage data for the 65+ age group, already adjusted according to the scenario definitions, are provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/vaccination/influenza_vax_scenarios.csv).

### Assumptions left to the modellers judgement
- Vaccination (and uptake levels) of at-risk individuals of all ages as well as vaccination of healthcare workers.
- We leave the implementation of the vaccination rollout to the discretion of the teams. This includes decisions on whether to use constant or time-varying administration rates and whether to administer most doses before the respiratory disease season
- VE against other endpoints
- Impact of seasonality, including seasonal behavioural changes.


### Data
We provide the following data to support models development and calibration.

Target data: 
- [historical ILI+](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/influenza/ili_plus.csv) data by age group and country

Vaccination data: 
- [Scenario vaccination coverage](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/vaccination/influenza_vax_scenarios.csv): vaccine coverage data for the 65+ age group to be used in the scenarios (i.e., already adjusted according to the scenario definitions) 

Auxiliary data: 
- [ILI](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/epidemiological/ILIconsultationrate.csv) and [ARI](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/epidemiological/ARIconsultationrate.csv) consultation rates
- [Vaccination for 65+](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/vaccination/vaccine_coverage_65plus.csv) (needed for scenario axis, more information above) and for all [other available age groups](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/vaccination/vaccine_coverage_all.csv)
- [Pathogen detections](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/miscellaneous/detections/pathogen_detection.csv)
- [Population](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/miscellaneous/population) by age group in different European countries

Additional references to external data sources that may be used for modeling are provided [here](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data)

