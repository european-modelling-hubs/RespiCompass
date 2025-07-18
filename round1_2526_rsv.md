# RSV - Round 1 2025/2026 Scenarios
- Submission deadline: 2025/12/01

### ⚠️⚠️⚠️ Warning
The repository is currently under construction for the 2025/2026 scenario round. All information is not final and subject to change until this message is removed.


## Background
### Infant RSV Burden in the EU/EEA
Respiratory Syncytial Virus (RSV) is a major cause of respiratory infections across the EU/EEA. The burden of disease is particularly high in older adults, individuals with underlying comorbidities, and young children [1-4]. Depending on the country, RSV-related hospitalisations have been estimated to account for 7% to 52% of all paediatric respiratory hospitalisations, representing approximately 250,000 annual hospital admissions in the entire EU/EEA [1]. Newborn babies have the highest per-capita rate of RSV-related hospitalisations [1].

### Recently Authorised Infant RSV Interventions
In October 2022, a new extended half-life monoclonal antibody, nirsevimab (Beyfortus®, AstraZeneca/Sanofi), was authorised in the EU for children up to 24 months of age  [5]. This product provides passive immunisation to protect neonates and infants who are vulnerable to severe RSV [6]. In June 2023, a maternal RSV vaccine (Abrysvo®, GSK) was also authorised in the EU [7]. Vaccination of pregnant individuals between 24 and 36 weeks of gestation has been shown to significantly reduce severe RSV-related respiratory infections in their infants during the first six months of life [8,9]. Additional RSV vaccines and extended half-life monoclonal antibodies are currently in phase 2/3 clinical trials, with clesrovimab (an extended half-life monoclonal antibody) having finished phase 3 trials and having been licensed by the FDA.

### Need for Modelling Evidence to Support Decision-Making
With the recent EU authorisation of these immunisation products, several EU/EEA countries have started or will soon begin the decision-making process on whether and how to introduce them into national programmes. Decisions on changing national immunisation programmes require consideration of multiple factors, including disease burden and epidemiology, the efficacy, effectiveness, and safety of new interventions, ease of implementation, population acceptance, and national health priorities. Mathematical and health economic modelling can support decision-making by estimating the potential impact of interventions on health outcomes and healthcare systems, projecting cost-effectiveness, exploring uncertainty, and supporting comparisons across policy options [10-13]. RespiCompass is designed to produce modelling evidence targeted at public health questions and to support ECDC guidance and assessments through ECDC-coordinated collaborative modelling.

### Scope of the RespiCompass 2025/26 RSV Scenario Round
The RespiCompass 2025/26 RSV Scenario round aims to support country-level health economic evaluations and decision-making around the introduction of universal RSV immunisation interventions for protecting newborns. The modelling scenarios focus on comparing the two newly-licensed options for immunising newborns against severe RSV - maternal vaccination or long-acting monoclonal antibodies - to a status-quo baseline without universal immunisation of newborns. For many EU/EEA countries this reflects the relevant decision-making questions of whether to introduce any RSV intervention, and which strategy to prioritise for newborn protection. 

Thus, this scenario round does not explicitely cover other uses for these products, including protections of older infants, or considerations around coverages for combined maternal vaccination and monoclonal antibody strategies. It will also not cover the impact of novel immunisation products targeting the RSV burden in older adults or of immunisation of at-risk newborns (while we are considering these immunisations as part of the status-quo strategy across scenarios). 

## RSV Modelling Scenarios

### Goal and Objectives
The overall goal of this scenario modelling round is to generate evidence supporting country-level decisions on the introduction of novel infant RSV immunisation strategies for protecting newborns. This will be achieved by comparing scenarios with universally offered maternal vaccination or scenarios with universally offered monoclonal antibodies for newborns against a status-quo (no universal intervention) baseline with respect to the following key outputs:
- Estimate of the seasonal infant RSV hospitalisations averted in the entire EU/EEA, and in individual EU/EEA countries. This reduction in the hospitalisation burden will be reported as a proportion and as a total number.

- Estimate of the number of infant hospitalisations averted per 100 infants immunised for the EU/EEA and at country-level, which can be converted into country-specific costs.

### Table of Scenarios
To achieve this goal, this project round will model five scenarios. This design allows for a clear comparison between the two primary interventions at different coverage levels and a baseline or status-quo counterfactual. In the following, we will use "la-mAbs" to refer to the new extended half-life monoclonal antibody and "MV" to refer to the new maternal RSV vaccine.

| | **High Coverage**. Coverage of the intervention assumed to be at 90% of the target population | **Low Coverage**. Coverage of the intervention assumed to be at 20% of the target population |
|  :-:|  :-: | :-: |
| **mAb only**. La-mAbs administered to newborns at birth starting on September $1^{st}$, 2025 and ending on March $31^{st}$, 2026 | Scenario A | Scenario B |
| **MV only**. MV administered during antenatal care visits, with immunization campaigns such that first immunized infants are born on $1^{st}$ of September, 2025 and the last immunized infants are born on $31^{st}$ of March, 2026 | Scenario C | Scenario D |
| **No Universal Immunisation**. No universal RSV immunisation is implemented $^*$.| Scenario E  (Baseline scenario) |  |

$^*$ Teams should use target data provided in the [target-data](./target-data/) folder to estimate typical country-specific RSV hospitalisation patterns in absence of universal interventions for newborns. In other words, the target data represents the baseline or status-quo scenario burden and models should be calibrated to match the target data as closely as possible in Scenario E.

The rationale for the proposed design is as follows:

- **Focus on single interventions (MV and mAbs)**: The scenario design focuses on comparing the two main options for immunising newborns against severe RSV (la-mAbs and MV) to a baseline scenario without universal interventions. This reflects the current decision-making landscape in the EU/EEA, where many countries are weighing whether to introduce any RSV intervention and which strategy to prioritise for newborn protection. It also maintains a symmetrical approach between the two immunisation options, allowing a fair comparison. 

- **Two coverage levels**: Expected immunisation coverage is a key uncertainty in any new immunisation programme. Modelling two distinct levels (low and high) for each intervention increases the country-relevance of the results. It also allows for an assessment of the linearity of impact with respect to coverage. The two identified coverage values were estimated based on the coverage of various proxy immunisation programmes across EU/EEA countries, as well as the early adoption of novel RSV interventions where implemented. 

- **Inclusion of a baseline scenario**: The proposal includes a baseline or status-quo scenario in which neither MV nor la-mAbs are universally given. However, we assume immunisation of at-risk newborns across all five scenarios if this is current country practice. This is needed to establish a counterfactual reference point for estimating the public health impact and added value of universal protection offered to newborns.

More broadly, this scenario round is designed not only to answer immediate policy questions but also to build RSV modelling capacity within the EU/EEA. In this sense, it aims to create a strong foundation for potential follow-up projects that could address more complex or country-specific questions in the future.


## Targets
Teams should use the target data provided in the [target-data](./target-data/) folder to estimate typical country-specific RSV hospitalisation patterns in absence of universal interventions. Requested modelling outputs or "targets" for all scenarios are: 
- **weekly RSV hospitalisation incidence** (i.e., new admissions) for each modelled country by age group (0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y, total) and immunisation status (yes, no, total) betweeen September $1^{st}$, 2025 and May $3^{rd}$, 2026. This target is **mandatory**.
- **weekly administered doses** for each modelled country betweeen September $1^{st}$, 2025 and May $3^{rd}$, 2026. In the case of la-mAbs, this target should be reported as the number of doses administered to newborns, on a given week and country. In the case of MV, this target should be reported as the number of doses administered to pregnant individuals, on a given week and country. This target is **mandatory**.
- **weekly RSV infection incidence** (i.e., new infections) in each individual countries by age group (0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y, total) and immunisation status (yes, no, total) betweeen September $1^{st}$, 2025 and May $3^{rd}$, 2026. This target is **optional**.

While teams may choose to submit targets for a subset of EU/EEA countries, we strongly encourage them to cover as many countries as possible. For each submitted country, we require teams to submit projections for all 5 scenarios and all modelled population groups (see [Submission Format](#submission-format) below).


## Shared Modelling Assumptions
The following assumptions must be shared by all contributing models:
- Immunisation effectiveness (IE) of la-mAbs is 87% (95% CI: 81-91%) against RSV-associated hospitalisations in infants based on meta-analysis presented in Ref. [14]. IE of MV is 78.6% (95% CI: 62.1–87.9%) against RSV-associated hospitalisations in infants based on Ref. [15]. We strongly encourage teams to include the uncertainty in the IE estimates in their modelling. For example, teams may sample IE values from the provided IE estimates and their uncertainty to generate scenario projections. 
- We assume no shortage of la-mAbs or MV in the EU/EEA at any time during the scenario period.
- The focus group for the universal intervention should be the newborns, and we aim to hamonise across the two immunisation options. Thus, immunisation coverage during intervention period should be as stated in the scenario table. We assume that immunisation campaigns are implemented in such a way that the first immunised infants are born on September $1^{st}$ and the last immunised infants are born on March $31^{st}$ of the next year. We leave it to the teams to decide on the time-varying coverage of the interventions, in the simplest case, this can be done by assuming a constant coverage over the intervention period. Different implementation strategies are allowed as long as the average coverage is consistent with the scenario axes, and as long as the time varying coverage is identical between the two immunisation options.
- We assume a common births cohort, specific for each country, for the scenario period. The data is provided [here](./auxiliary-data/births/).
- We assume no universal RSV intervention in the senior population (e.g., RSV senior vaccine) are implemented during the scenario period and that the target data is representative of the typical RSV hospitalisation patterns in absence of such interventions.
- An RSV immunisation option for at-risk newborns (palivizumab, a short half-life monoclonal antibody) has been available in the EU/EEA since 1999. This intervention is not focus of this investigation. Therefore, for countries where palivizumab has been part of clinical practice [16], we assume that it is used across all scenarios (or replaced by long-acting antibodies and assuming identical impact). For countries where palivizumab has not been in use, we assume this also to be the case across scenarios. Impact of palivizumab is assumed to be part of the background immunity and should not be explicitly modelled, as its impact is already reflected in the target data. Modellers should model and report la-mAbs doses given to all newborns (at-risk and others). In our post-hoc analysis of incremental impact of universal newborn immunsation, we will then account for the fact that in some countries and scenarios la-mAbs are both replacing short half-live antibodies as well as being offered to all newborns.
- We acknowledge that fetal, perinatal, and neonatal mortality may have a minor effect on immunisation coverage and impact. However, these rates are very low (less than 1%; see [17]) and can therefore reasonably be considered negligible by teams for the purposes of this scenario round.


## Modelling Assumptions Left to the Modellers Judgement
- We encourage teams to account for waning of immunisation-induced protection at their discretion. To support this, we provide additional information and evidence [here](./auxiliary-data/waning/).
- Additional effects of the interventions, such as the reduced infectiousness of vaccinated individuals if they become infected, protection against infection, are allowed and encouraged but left to the modellers judgement. We refer the teams to the [auxiliary-data](./auxiliary-data/Readme.md) readme for additional information on available evidence on the effects of the modelled interventions.
- While la-mAbs are administered at birth, MVs are administered during antenatal care visits between 24 and 36 weeks of gestation. We leave the model details concerning immunisation of pregnant individuals (including precise timing and immunisation effect in those individuals) to the discretion of the modelling teams.   
- Teams can include demographic effects, including age-specific mortality (e.g., non-RSV related), in their models. To support this, we provide additional information and evidence [here](./auxiliary-data#demographic-effects).


## Auxiliary Data
We provide the following data to support model development and calibration: 
- Weekly RSV hospitalisations (i.e., new admissions) are provided for each country over the modelling period in the absence of universal RSV interventions. This data must be used to calibrate models to the baseline scenario (Scenario E). Weekly hospitalisation counts are given for the total population, with additional aggregated estimates by age group. Models should aim to reproduce the target data as closely as possible, capturing both the overall seasonal patterns and age-specific burdens. Available [here](./target-data/). 
- Population data by age group and country. This information has to be intended as the resident population of the country in different age groups at the start of the modelling period. Available [here](./auxiliary-data/population/).
- Monthly births data by country. This information has to be intended as the number of births in the country in each month of the modelling period. Available [here](./auxiliary-data/births/).
- List of countries, available [here](./supporting-files/countries.csv).
- List of weeks in the modelling period, available [here](./supporting-files/isoweeks.csv).

## Submission Format
General guidance for the submission format is provided in the [Wiki](https://github.com/european-modelling-hubs/RespiCompass/wiki/Submission-format). For this specific round, submission file must be saved in [parquet format](https://parquet.apache.org/) and named

```2025_2026_1_RSV-<team>-<model>.parquet```

Where `<team>-<model>` will be specific for each team/model and must match the `team_abbr` and `model_abbr` parameters in the metadata file. Additionally, you should set: 
-  ```round_id = '2025_2026_1_RSV'```
-  ```scenario_id```: allowed values are ```'A', 'B', 'C', 'D', 'E'``` related to different scenarios
-  ```target = 'rsv_hospitalisations'```,  ```'administered_doses'```, ```'rsv_infections'```, which denote weekly new RSV hospitalisations, doses administered or infections.
-  ```pop_group``` allowed values are ```'0-2mo_immYes', '0-2mo_immNo', '0-2mo_immTotal', '3-5mo_immYes', '3-5mo_immNo', '3-5mo_immTotal', '6-11mo_immYes', '6-11mo_immNo', '6-11mo_immTotal', '1-4y_immYes', '1-4y_immNo', '1-4y_immTotal', '5-64y_immYes', '5-64y_immNo', '5-64y_immTotal', '65+y_immYes', '65+y_immNo', '65+y_immTotal', 'total_immYes', 'total_immNo', 'total_immTotal'```, and ```None``` (when ```target='administered_doses'```, see below), covering all combinations of considered age groups and immunisation status that are the source population for the weekly incidence. Note that groups ```immYes``` are individuals that were immunised prior to the hospitalisation or infection (i.e., la-mAbs or MV) during the scenario period. In the case of scenarios considering la-mAbs, the ```immYes``` groups will be made up of the newborns that received la-mAbs at birth. In the case of scenarios considering MV, the ```immYes``` groups will be made up of the mothers that received MV during the scenario period and their newborns. When ```target='administered_doses'``` leave ```pop_group``` blank.
- ```horizon```: weeks ahead in the projection period, see [here](./supporting-files/isoweeks.csv) for a horizon/week correspondence
- ```target_end_date``` end date of target week, see [here](./supporting-files/isoweeks.csv) for a date/week correspondence
- ```output_type```: we request teams to submit 300 individual trajectories for each scenario. For trajectories ```output_type='sample'```.
- ```output_type_id```: '1' to '300' for samples. In cases where “matched” trajectories are used (i.e., trajectories that share the same parameter set across different scenarios), the same ```output_type_id``` should be assigned across those scenarios to maintain consistency.

# Contacts
If you have any question regarding this scenario round do not hesitate to get in touch at [rsv-respicompass@isi.it](mailto:rsv-respicompass@isi.it).


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
14. Xiao Li, Roberfroid Dominique, Bilcke Joke, Castanares-Zapatero Diego, de Meester Christophe, Mao Zhuxin, Thiry Nancy, Willem Lander, Beutels Philippe. Cost-effectiveness of new preventive options against RSV infections in Belgian infants. Health Technology Assessment (HTA). Brussels. Belgian Health Care Knowledge Centre (KCE). 2025. KCE Reports 402C. DOI: 10.57598/R402C. Available at: https://kce.fgov.be/en/publications/all-reports/cost-effectiveness-of-new-preventive-options-against-rsv-infections-in-belgian-infants
15. Marc GP, Vizzotti C, Fell DB, Di Nunzio L, Olszevicki S, Mankiewicz SW, Braem V, Rearte R, Atwell JE, Bianchi A, Fuentes N. Real-world effectiveness of RSVpreF vaccination during pregnancy against RSV-associated lower respiratory tract disease leading to hospitalisation in infants during the 2024 RSV season in Argentina (BERNI study): a multicentre, retrospective, test-negative, case–control study. The Lancet Infectious Diseases. 2025 May 5. Available at: https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(25)00156-2/abstract
15. Reeves, R.M., van Wijhe, M., Lehtonen, T., Stona, L., Teirlinck, A.C., Vazquez Fernandez, L., Li, Y., Osei-Yeboah, R., Fischer, T.K., Heikkinen, T. and Van Boven, M., 2022. A systematic review of European clinical practice guidelines for respiratory syncytial virus prophylaxis. The Journal of infectious diseases, 226(Supplement_1), pp.S110-S116. Available at: https://academic.oup.com/jid/article/226/Supplement_1/S110/6554001 
16. Eurostat. Fetal, peri- and neonatal mortality rates by country of occurrence. 2025. Available at: https://ec.europa.eu/eurostat/databrowser/view/hlth_cd_aperrto/default/table?lang=en. DOI: https://doi.org/10.2908/HLTH_CD_APERRTO
