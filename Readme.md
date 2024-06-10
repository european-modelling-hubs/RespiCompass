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
TODO

### Targets and Submission Format
We are currently asking for ILI+ weekly between August 1, 2024 and May 31, 2025 in European countries. The list of countries is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/locations_iso2_codes.csv) and the list of weeks is provided [here](TODO). ILI+ is computed as follows:

$$ILI+ = ILI \times \frac{Positivity_{Influenza}}{100}$$

Where ILI is the consulation rate for influenza-like-illness reported in a given country and week, and $Positivity_{Influenza}$ is the test positivity rate for influenza (overall, without considering subtypes) from either sentinel or non-sentinel detections in that country and week. All countries consider sentinel surveillance except for Malta, Iceland, Croatia, Romania, Latvia, Finland, where non-sentinel detections are considered. Historical ILI+ data is provided [here](https://github.com/european-modelling-hubs/RespiCompass/blob/main/target-data/influenza/ili_plus.csv).

### Data
TODO

## COVID-19 - Round 1 2024/2025 Scenarios
| | Optimistic waning (Protection against infection: 6 months median time to transition to 70% of the initial immunity; Protection against severe outcomes: no waning) | Pessimistic waning (Protection against infection: 6 months median time to transition to 40% of the initial immunity; Protection against severe outcomes: 6 months median time to transition to 80% of the initial immunity) |
|  :-:|  :-: | :-: |
| Higher than usual Vaccine Coverage (Vaccine coverage is 15% higher than in the 2023-24 winter season in 65+ in all countries) | Scenario A | Scenario B |
| Lower than usual Vaccine Coverage (Vaccine coverage is 15% lower than in the 2023-24 winter season in 65+ in all countries) | Scenario C | Scenario D |
| No Vaccination (baseline scenario without vaccination) | Scenario E | Scenario F |

### Shared Assumptions
TODO

### Targets and Submission Format
TODO

### Data
TODO
