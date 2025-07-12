# RSV - Round 1 2025/2026 Scenarios
- Submission deadline: 2025/XX/XX

### ⚠️⚠️⚠️ Warning
The repository is currently under construction for the 2025/2026 scenario round. All information is not final and subject to change until this message is removed.


## Background
### RSV Burden in the EU/EEA
Respiratory Syncytial Virus (RSV) is a major cause of respiratory infections across the EU/EEA. The burden of disease is particularly high in older adults, individuals with underlying comorbidities, and young children [1-4]. Depending on the country, RSV-related hospitalisations account for 7% to 52% of all paediatric respiratory hospitalisations, representing approximately 250,000 annual hospital admissions in the entire EU/EEA [1]. Approximately 75% of these cases occur in infants under one year of age [1].

### Recently Authorised Infant RSV Interventions
In October 2022, a new extended half-life monoclonal antibody, nirsevimab (Beyfortus®, AstraZeneca/Sanofi), was authorised in the EU [5]. This product provides passive immunisation to protect infants during their first RSV season [6]. In June 2023, a maternal RSV vaccine (Abrysvo®, GSK) was also authorised in the EU [7]. Vaccination of pregnant individuals between 24 and 36 weeks of gestation has been shown to significantly reduce severe RSV-related respiratory infections in their infants during the
first six months of life [8,9]. Additional RSV vaccines and extended half-life monoclonal antibodies are currently in phase 2/3 clinical trials.

### Need for Evidence to Support Decision-Making
With the recent EU authorisation of these immunisation products, several EU/EEA countries have started or will soon begin the decision-making process on whether and how to introduce them into national programmes. Decisions on changing national immunisation programmes require consideration of multiple factors, including disease burden and epidemiology, the efficacy, effectiveness, and safety of new interventions, ease of implementation, population acceptance, and national health priorities. Mathematical and health economic modelling can support decision-making by estimating the potential impact of interventions on health outcomes and healthcare systems, projecting cost-effectiveness, exploring uncertainty, and supporting comparisons across policy options [10-13].

### The RespiCompass 2025/26 RSV Scenario Round
The RespiCompass 2025/26 RSV Scenario round aims to produce evidence through ECDC-coordinated collaborative modelling on the population-level impact of the new infant RSV immunisation interventions. The project will produce outputs designed to support country-level health economic evaluations and decision-making around the introduction of these products. This project round will focus exclusively on universal infant immunisation strategies. It will not cover novel immunisation products targeting the RSV burden in older adults or strategies specifically targeting at-risk newborns.

## RSV Modelling Scenarios

### Goal and Objectives
The overall goal of this scenario modelling round is to generate evidence supporting country-level decisions on the introduction of novel infant RSV immunisation strategies. This will be achieved comparing scenarios with maternal vaccination or scenarios with monoclonal antibodies against no-intervention baselines with respect to the following key outputs:
- Estimate of the seasonal RSV hospitalisations averted in the entire EU/EEA, and in individual EU/EEA countries. This reduction in the hospitalisation burden will be reported as a proportion and as a total number.

- Estimate of the number of infant hospitalisations averted per 100 infants immunised for the EU/EEA and at country-level, which can be converted into country-specific costs.

### Table of Proposed Scenarios
To achieve this goal, this project round will model the following five scenarios. This structure allows for a clear comparison between the two primary interventions at different coverage levels and a baseline counterfactual. At the same time, the scenario selection accounts for the resource constraints of this project that strongly limits the possible number of modelling scenarios. In the following, we will use "la-mAbs" to refer to the new extended half-life monoclonal antibody and "MV" to refer to the new maternal RSV vaccine.

| | **High Coverage**. Coverage of the intervention assumed to be at 80% of the target population | **Low Coverage**. Coverage of the intervention assumed to be at 20% of the target population |
|  :-:|  :-: | :-: |
| **mAb only**. La-mAbs administered to newborns at birth starting on September $1^{st}$ and ending on March $31^{st}$ of the next year | Scenario A | Scenario B |
| **MV only**. MV administered during antenatal care visits, with immunization campaigns such that first immunized infants are born on $1^{st}$ of September and the last immunized infants are born on $31^{st}$ of March of the next year | Scenario C | Scenario D |
| **No Immunisation**. No intervention is implemented, all infants remain at risk of RSV infection and hospitalization based on historical transmission patterns $^*$.| Scenario E  (Baseline scenario) |  |

$^*$ Teams should use target data provided in the [target-data](./target-data/) folder to estimate typical hospitalisation patterns in absence of interventions. In other words, the target data is the baseline scenario and models should be calibrated to match the target data as closely as possible in Scenario E.

The selection of these scenarios is guided by the need to prioritise the most pressing policy questions within the project's resource constraints. The rationale for the proposed design is as follows:

- **Focus on single interventions (MV and mAbs)**: The scenario design focuses on comparing the two main options for immunising infants against severe RSV (maternal vaccination and monoclonal antibodies) to a no-intervention baseline. This reflects the current decision-making landscape in the EU/EEA, where many countries are weighing whether to introduce any RSV intervention and which strategy to prioritise for newborn protection.

- **Two coverage levels**: Expected immunisation coverage is a key uncertainty in any new immunisation programme. Modelling two distinct levels (low and high) for each intervention increases the country-relevance of the results. It also allows for an assessment of the linearity of impact with respect to coverage.

- **Inclusion of a baseline scenario**: The proposal includes a baseline scenario in which neither MV nor mAbs are implemented. This is essential to establish a counterfactual reference point for estimating the public health impact and added value of the novel interventions.

Additionally, this focused scenario round is designed not only to answer immediate policy questions but also to build RSV modelling capacity within the EU/EEA. It will create a strong foundation for potential follow-up projects that could address more complex or country-specific questions in the future.


## Targets
Teams should use the target data provided in the [target-data](./target-data/) folder to estimate typical hospitalisation patterns in absence of interventions in different countries. Requested targets for the different scenarios are: 
- weekly RSV hospitalisations (i.e., new admissions) in each individual countries by age group (0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y, total) and immunisation status (yes, no, total) betweeen September $1^{st}$, 2025 and April $30^{th}$, 2026. This target is mandatory for all teams.
- weekly RSV infections in each individual countries by age group (0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y, total) and immunisation status (yes, no, total) betweeen September $1^{st}$, 2025 and April $30^{th}$, 2026. This target is optional for all teams.

While teams may choose to submit targets for only a subset of countries, we strongly encourage them to cover as many countries as possible.


## Shared Assumptions
We will consider the following assumptions to be shared by all teams:
- VE of la-mAbs is 87% (95% CI: 81-91%) against RSV-associated hospitalisations in infants. VE of MV is XX% (95% CI: XX-XX) against RSV-associated hospitalisations in infants. We encourage teams to include the uncertainty in the VE estimates in their modelling. For example, teams may sample VE from the provided VE estimates and their uncertainty to generate scenario projections. 
- We assume no shortage of la-mAbs or MV in the EU/EEA at any time during the scenario period.
- Vaccination coverage as outlined in the scenario axes. We assume that immunisation campaigns are implemented in a way that the first immunised infants are born on September $1^{st}$ and the last immunised infants are born on March $31^{st}$ of the next year. We leave to the teams to decide on the time-varying coverage of the interventions, in the simplest case, this can be done by assuming a constant coverage over the scenario period. Different implementation strategies are allowed as long as the overall coverage is consistent with the scenario axes.
- We assume a common births cohort, specific for each country, for the scenario period. The data is provided [here](./auxiliary-data/births/).
- We assume no senior interventions (e.g., RSV senior vaccine) are implemented during the scenario period and that the target data is representative of the typical RSV hospitalisation patterns in absence of such interventions.
- Although another preventive option (palivizumab, a monoclonal antibody for high-risk infants) is available in the EU/EEA, it is not included in this scenario round, as its impact is assumed to be already reflected in the target data and negligible at the population level.


## Assumptions Left to the Modellers Judgement
- We encourage teams to account for waning of immunisation-induced protection at their discretion. To support this, we provide additional information and evidence in the [XXX](LINK) folder.
- Additional effects of the interventions, such as the reduced infectiousness of vaccinated individuals if they become infected, protection against infection, are allowed and encouraged but left to the modellers judgement. We refer the teams to the [XXX](LINK) folder for additional information on available evidence on the effects of the modelled interventions.


## Auxiliary Data
We provide the following data to support models development and calibration: 
- Weekly RSV hospitalisations (i.e., new admissions) are provided for each country over the modelling period in the absence of interventions. This data must be used to calibrate models to the baseline scenario (Scenario E). Weekly hospitalisation counts are given for the total population, with additional aggregated estimates by age group. Models should aim to reproduce the target data as closely as possible, capturing both the overall seasonal patterns and age-specific burdens. Available [here](./target-data/). 
- Population data by age group and country. This information has to be intended as the resident population of the country in different age groups at the start of the modelling period. Available [here](./auxiliary-data/population/).
- Monthly births data by country. This information has to be intended as the number of births in the country in each month of the modelling period. Available [here](./auxiliary-data/births/).
- List of countries, available [here](./supporting-files/countries.csv).
- List of weeks in the modelling period, available [here](./supporting-files/weeks.csv).

## Submission Format
General guidance for the submission format is provided in the [Wiki](https://github.com/european-modelling-hubs/RespiCompass/wiki/Submission-format). For this specific round, submission file must be saved in [parquet format](https://parquet.apache.org/) and named

```2025_2026_1_RSV-<team>-<model>.parquet```

Where `<team>-<model>` will be specific for each team/model and must match the `team_abbr` and `model_abbr` parameters in the metadata file. Additionally, you should set: 
-  ```round_id = '2025_2026_1_RSV'```
-  ```scenario_id```: allowed values are ```'A', 'B', 'C', 'D', 'E'``` related to different scenarios
-  ```target = 'rsv_hospitalisations'``` or ```'rsv_infections'```
-  ```pop_group``` allowed values are ```'0-2mo_immYes', '0-2mo_immNo', '0-2mo_immTotal', '3-5mo_immYes', '3-5mo_immNo', '3-5mo_immTotal', '6-11mo_immYes', '6-11mo_immNo', '6-11mo_immTotal', '1-4y_immYes', '1-4y_immNo', '1-4y_immTotal', '5-64y_immYes', '5-64y_immNo', '5-64y_immTotal', '65+y_immYes', '65+y_immNo', '65+y_immTotal', 'total_immYes', 'total_immNo', 'total_immTotal'```, covering all combinations of considered age groups and vaccination status. Note that groups ```immYes``` are individuals that were immunised prior to the hospitalisation or infection (i.e., la-mAbs or MV) during the scenario period. In the case of scenarios considering la-mAbs, the ```immYes``` groups will be made up of the newborns that received la-mAbs at birth. In the case of scenarios considering MV, the ```immYes``` groups will be made up of the mothers that received MV during the scenario period and their newborns.
- ```horizon```: weeks ahead in the projection period, see [here](./supporting-files/isoweeks.csv) for a horizon/week correspondence
- ```target_end_date``` end date of target week, see [here](./supporting-files/isoweeks.csv) for a date/week correspondence
- ```output_type```: we request teams to submit 300 individual trajectories for each scenario. For trajectories ```output_type='sample'```.
- ```output_type_id```: '1' to '300' for samples. ADD INFO ON MATCHED TRAJECTORIES.


# References
1. Del Riccio M, Spreeuwenberg P, Osei-Yeboah R, Johannesen CK, Fernandez LV, Teirlinck AC, et al. Burden of Respiratory Syncytial Virus in the European Union: estimation of RSV-associated hospitalizations in children under 5 years. J Infect Dis. 2023 2023/11/28;228(11):1528-38. Available at: https://www.ncbi.nlm.nih.gov/pubmed/37246724
2. Osei-Yeboah R, Spreeuwenberg P, Del Riccio M, Fischer TK, Egeskov-Cavling AM, Bøås H, et al. Estimation of the number of respiratory syncytial virus-associated hospitalizations in adults in the European Union. J Infect Dis. 2023 2023/11/28;228(11):1539-48. Available at: https://www.ncbi.nlm.nih.gov/pubmed/37246742
3. Savic M, Penders Y, Shi T, Branche A, Pirçon J-Y. Respiratory syncytial virus disease burden in adults aged 60 years and older in high-income countries: A systematic literature review and meta-analysis. Influenza Other Respi Viruses. 2023 2023/1;17(1):e13031. Available at: https://www.ncbi.nlm.nih.gov/pubmed/36369772
4. Nguyen-Van-Tam JS, O&#39;Leary M, Martin ET, Heijnen E, Callendret B, Fleischhackl R, et al. Burden of respiratory syncytial virus infection in older and high-risk adults: a systematic review and meta-analysis of the evidence from developed countries. Eur Respir Rev. 2022 2022/12/31;31(166):220105. Available at: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9724807
5. European Medicines Agency (EMA). Beyfortus - nirsevimab. 2022. Available at: https://www.ema.europa.eu/en/medicines/human/EPAR/beyfortus
6. Sumsuzzman D, Wang Z, Langley JM, Moghadas SM. Real-world effectiveness of nirsevimab against respiratory syncytial virus disease in infants: A systematic review and meta-analysis. Social Science Research Network. 2025 2025/1/15 Available at: https://dx.doi.org/10.2139/ssrn.5096762 
7. European Medicines Agency (EMA). Abrysvo. 2023. Available at: https://www.ema.europa.eu/en/medicines/human/EPAR/abrysvo
8. Mapindra MP, Mahindra MP, McNamara P, Semple MG, Clark H, Madsen J. Respiratory syncytial virus maternal vaccination in infants below 6 months of age: Meta-analysis of safety, immunogenicity, and efficacy. Neonatology. 2024 2024/1/29;121(3):271-82. Available at: https://dx.doi.org/10.1159/000536031
9. Pérez Marc G, Vizzotti C, Fell DB, Di Nunzio L, Olszevicki S, Mankiewicz SW, et al. Real-world effectiveness of RSVpreF vaccination during pregnancy against RSV-associated lower respiratory tract disease leading to hospitalisation in infants during the 2024 RSV season in Argentina (BERNI study): a multicentre, retrospective, test-negative, case-control study. Lancet Infect Dis. 2025 2025/5/5;0(0) Available at: http://dx.doi.org/10.1016/S1473-3099(25)00156-2
10. Nohynek H, Wichmann O, D Ancona F, Gatekeepers VN. National Advisory Groups and their role in immunization policy-making processes in European countries. Clin Microbiol Infect. 2013 2013/12;19(12):1096-105. Available at: http://dx.doi.org/10.1111/1469-0691.12315
11. European Centre for Disease Prevention and Control (ECDC). Current practices in immunisation policymaking in European countries. 2015 2015/3/5 Available at: https://www.ecdc.europa.eu/en/publications-data/current-practices-immunisation-policymaking-european-countries
12. Runge MC, Shea K, Howerton E, Yan K, Hochheiser H, Rosenstrom E, et al. Scenario design for infectious disease projections: Integrating concepts from decision analysis and experimental design. Epidemics. 2024 2024/6;47(100775):100775. Available at: https://www.ncbi.nlm.nih.gov/pubmed/38838462
13. Shea K, Borchering RK, Probert WJM, Howerton E, Bogich TL, Li S-L, et al. Multiple models for outbreak decision support in the face of uncertainty. Proc Natl Acad Sci U S A. 2023 2023/5/2;120(18):e2207537120. Available at: https://pnas.org/doi/10.1073/pnas.2207537120
