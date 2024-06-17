## Influenza - Round 1 2024/2025 Scenarios
### Deadline
- Submission deadline: 2024/08/31 (after this date a first report for 2024/25 respiratory diseases insights will be drafted with available models' projections)
- Late submissions deadline: 2024/09/20 (draft report will be revised after this date considering all models' projections)

### Rationale
We aim to explore the potential impact of Influenza during the upcoming 2024-2025 respiratory disease season. To this end, we have designed a set of scenarios that examine two main axes:
- **Impact of Higher/Lower Vaccination Coverage in the Target Population (65+)**: with these assumptions we want to test the impact of seasonal vaccination campaigns on influenza spread and burden. More in detail, we seek to understand the space of effectiveness of policies aimed at improving coverage in at-risk groups.
- **Impact of higher/lower transmission potential**: with these assumptions we want to test the impact of potential changes in transmission potential from season to season. 

Ultimately, we also want to explore the interactions between these two dimensions and, for instance, we aim to examine how an actionable increase in vaccination coverage in target groups might counterbalance variations in transmission potential from one season to the next.

### Scenarios
| | Lower Burden Season (Transmission potential* is 10% lower with respect to average of last three influenza seasons (excluding pandemic years) | Higher Burden Season (Transmission potential is 10% higher with respect to average of last three influenza seasons, excluding pandemic years) |
|  :-:|  :-: | :-: |
| Higher than usual Vaccine Coverage (Vaccine coverage is 15% higher than last flu season with available data in 65+ in all countries) | Scenario A | Scenario B |
| Lower than usual Vaccine Coverage (Vaccine coverage is 15% lower than last flu season with available data in 65+ in all countries) | Scenario C | Scenario D |
| No Vaccination (baseline scenario without vaccination) | Scenario E | Scenario F |

*Teams should use data from the last three influenza seasons (2017-2018, 2018-2019, and 2023-2024 excluding pandemic years) to estimate an average transmission potential (e.g., $R_t$) and assume it to be +/- 10%. Transmission potential includes all factors that may impact transmission rate, except for vaccination coverage, which is captured by the other scenario axis. 

### Targets
We are currently asking for ILI+ weekly between August 1, 2024 and May 31, 2025 in European countries by age groups (0-4, 5-14, 15-64, 65+, total) and vaccination status (yes, no)

The list of countries is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/locations_iso2_codes.csv) and the list of weeks is provided [here](TODO). ILI+ is computed as follows:

$$ILI+ = ILI \times \frac{Positivity_{Influenza}}{100}$$

Where ILI is the consulation rate for influenza-like-illness reported in a given country and week, and $Positivity_{Influenza}$ is the test positivity rate for influenza (overall, without considering subtypes) from either sentinel or non-sentinel detections in that country and week. All countries consider sentinel surveillance except for Malta, Iceland, Croatia, Romania, Latvia, Finland, where non-sentinel detections are considered. Historical ILI+ data is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/influenza/ili_plus.csv). The rationale for using ILI+ instead of ILI is rooted in the increased non-specificity of ILI, particularly after the advent of COVID-19. By combining ILI with detection rates, we obtain a signal more specific to influenza.

### Submission Format

### Shared Assumptions
#### Vaccine Effectiveness (VE)
For all scenarios we assume a VE = 40% against infection based on available literature (see [here](https://docs.google.com/document/d/1RKkT9aYD5D8tsRYE1-jQ1jUDhckEWxIhMQ9plO1dk_c/edit?usp=sharing) for list of studies considered). For this round we assume the same VE for all age groups.
Teams may, at their discretion, include additional effects of vaccines, such as the reduced infectiousness of vaccinated individuals if they become infected.

#### Vaccine Coverage and Rollout
In scenarios A and B, we assume vaccination coverage for the 65+ age group is 15% higher compared to the data reported during the last season for which data is available (2021/2022 for most of the countries). This represents a relative increase, meaning that a coverage of 50% would increase to 57.5%.

In scenarios C and D, we assume vaccination coverage for the 65+ age group is 15% lower compared to the data reported during the last season for which data is available

We advise that teams maintain vaccination coverage in other age groups at the same levels as the last season for which data is available. If data on vaccination coverage in other age groups are not available, teams can make assumptions, provided the coverage remains lower than that of the 65+ (at-risk) population.

Scenarios E and F are hypothetical scenarios where teams are asked not to include vaccinations in any age groups. These scenarios are used to estimate the effect of vaccinations against a baseline scenario in which they are completely absent.

We leave the implementation of the vaccination rollout to the discretion of the teams. This includes decisions on whether to use constant or time-varying administration rates and whether to administer most doses before the respiratory disease season.

Vaccine coverage data for the 65+ age group, already adjusted according to the scenario definitions, are provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/auxiliary-data/influenza/vaccination/influenza_vax_scenarios.csv).


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

