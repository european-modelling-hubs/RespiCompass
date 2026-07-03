# RSV - Round 1 2026/2027 Scenarios

## Background
### Respiratory Syncytial Virus
Respiratory Syncytial Virus (RSV) is a common virus that causes infections of the respiratory tract, particularly in young children, older adults, and immunocompromised individuals. RSV is easily transmitted and spreads through respiratory droplets, direct contact, or contaminated surfaces. Recurrent yearly waves of infections and associated hospitalisations are observed, with seasonality varying across the world [1].

Despite its well documented impact on children, RSV burden in adults remains underexplored, partly due to limited PCR testing before the COVID-19 pandemic. In adults, RSV can present across a wide spectrum, from no symptoms at all or mild respiratory illness to serious lower respiratory tract infections [2,3]. Among older adults and those with pre-existing health conditions, the infection can be severe enough to require hospitalisation and, in some cases, may prove fatal [4].

### RSV burden in adults in Europe
RSV imposes a significant health and economic burden across Europe. On average, 160,000 RSV-associated hospitalisations occur annually among adults in Europe (≥18 years), 92% of these hospitalisations occur in adults ≥65 years [5]. Among 75–84 years, the annual average is estimated at 74,500, while among ≥85 years, the annual average is estimated at 37,900 [5]. In comparison, the estimate in adults is lower but of a similar magnitude to the estimate in young children (0–4 years), which is approximately 245,000 [6].

RSV circulation in Europe was significantly affected by the introduction of non-pharmaceutical interventions (NPIs) and other restrictions in response to the COVID-19 pandemic. Following the lifting of these measures, many countries experienced atypical RSV activity, characterised by out-of-season surges and intensified peaks, likely driven by a build-up of population susceptibility resulting from reduced circulation during the time of COVID-19 related restrictions. More recent data suggests that RSV seasonality in many regions is transitioning back towards pre-pandemic norms.

### Recently Authorised Adult RSV Interventions
In the last three years, several RSV immunisation products have been authorised in the EU. The European Commission approved GSK's Arexvy vaccine in June 2023 for individuals aged 60 and above, marking it as the first RSV vaccine for this demographic. In 2026, it received extended approval for adults 18 and older. Moderna's mRNA-based vaccine, mRESVIA, and Pfizer's Abrysvo also received approval for adults aged 18 and older. Following the approval of these novel immunisation products, multiple EU/EEA member states have started the process of national implementation decisions, resulting in varied approaches across the EU/EEA with respect to eligibility age, risk-group restrictions, and funding.

### Need for Modelling Evidence to Support Decision-Making
With the recent EU authorisation of these immunisation products, several EU/EEA countries have started or will soon begin the decision-making process on whether and how to introduce them into national programmes. Decisions on changing national immunisation programmes require consideration of multiple factors, including disease burden and epidemiology, the efficacy, effectiveness, and safety of new interventions, ease of implementation, population acceptance, and national health priorities. Mathematical and health economic modelling can support decision-making by estimating the potential impact of interventions on health outcomes and healthcare systems, projecting cost-effectiveness, exploring uncertainty, and supporting comparisons across policy options. RespiCompass is designed to produce modelling evidence targeted at public health questions and to support ECDC guidance and assessments through ECDC-coordinated collaborative modelling.

### Scope of the RespiCompass 2026/27 RSV Scenario Round
The RespiCompass 2026/27 RSV Scenario round aims to support country-level health economic evaluations and decision-making around the introduction of universal RSV immunisation interventions for protecting older adults.


## RSV Modelling Scenarios

### Goal and Objectives
The goal of this round of RespiCompass is to provide modelling evidence supporting country-level decisions on the introduction of novel RSV immunisation strategies for protecting older adults. This will be achieved by comparing scenarios with universally offered adult vaccination against a status-quo (no universal intervention) baseline. In more detail, this round will aim to answer the following questions:
1. Should one dose of RSV vaccine be recommended for all adults ≥60, ≥65, ≥70, ≥75, ≥80 years of age and older?
2. What is the expected impact of varying duration of protection following a single dose, and when might re-vaccination be considered in different age groups?

### Table of Scenarios
To jointly address both questions, this round explores the full combination of eligibility age thresholds and durations of immunity as a single set of scenarios, rather than as two sequential steps. Each cell of the table below corresponds to one scenario, combining a minimum eligibility age for universal immunisation with an assumed duration of vaccine-induced immunity.

| | **Eligibility Age** ≥60 | ≥65 | ≥70 | ≥75 | ≥80 |
|  :-:|  :-: | :-: | :-: | :-: | :-: |
| **Duration of Immunity**: 6 months  | A.1 | A.2 | A.3 | A.4 | A.5 |
| **Duration of Immunity**: 12 months | B.1 | B.2 | B.3 | B.4 | B.5 |
| **Duration of Immunity**: 18 months | C.1 | C.2 | C.3 | C.4 | C.5 |
| **No Universal Immunisation**. No universal RSV immunisation is implemented.$^*$ | Scenario F  (Baseline scenario) | | | | |

$^*$ Teams should use target data provided in the [target-data](./target-data/) folder to estimate typical country-specific RSV hospitalisation patterns in absence of universal interventions. In other words, the target data represents the baseline or status-quo scenario burden and models should be calibrated to match the target data as closely as possible in Scenario F.


## Targets
Teams should use the target data provided in the [target-data](./target-data/) folder to estimate typical country-specific RSV hospitalisation patterns in absence of universal interventions. Requested modelling outputs or "targets" for all scenarios are: 
- **weekly RSV hospitalisation incidence** (i.e., new admissions) for each modelled country by age group (0-2mo, 3-5mo, 6-11mo, 1-4, 5-17, 18-59, 60-64, 65-69, 70-74, 75-79, 80+, total) and immunisation status (yes, no, total) between September $1^{st}$, 2026 and August $31^{st}$, 2027. This target is **mandatory**.
- **weekly administered doses** for each modelled country, on a given week and country, between September $1^{st}$, 2026 and August $31^{st}$, 2027. This target is **mandatory**.
- **weekly RSV infection incidence** (i.e., new infections) in each individual countries by age group (0-2mo, 3-5mo, 6-11mo, 1-4, 5-17, 18-59, 60-64, 65-69, 70-74, 75-79, 80+, total) and immunisation status (yes, no, total) between September $1^{st}$, 2026 and August $31^{st}$, 2027. This target is **optional**.

While teams may choose to submit targets for a subset of EU/EEA countries, we strongly encourage them to cover as many countries as possible. For each submitted country, we require teams to submit projections for all modelled scenarios and all modelled population groups (see [Submission Format](#submission-format) below).


## Shared Modelling Assumptions
The following assumptions must be shared by all contributing models:
- We assume a common births cohort, specific for each country, for the scenario period. The data is provided [here](./auxiliary-data/births/).
- We assume no universal RSV intervention in the infant population (e.g., la-mAbs, maternal vaccination) are implemented during the scenario period and that the target data is representative of the typical RSV hospitalisation patterns in absence of such interventions.


## Modelling Assumptions Left to the Modellers Judgement
- Teams can include demographic effects, including age-specific mortality (e.g., non-RSV related), in their models. To support this, we provide additional information and evidence [here](./auxiliary-data#demographic-effects).


## Auxiliary Data
Through this github repository we provide and point toward all data that is essential for the modelling. No ECDC data requests are required for this project. We provide the following to support model development and calibration: 

- Weekly RSV hospitalisations (i.e., new admissions) are provided for each country over the modelling period in the absence of universal RSV interventions. This data must be used to calibrate models to the baseline scenario. Weekly hospitalisation counts are given for the total population, with additional aggregated estimates by age group. Models should aim to reproduce the target data as closely as possible, capturing both the overall seasonal patterns and age-specific burdens. Available [here](./target-data/). 
- Population data by age group and country. This information has to be intended as the resident population of the country in different age groups at the start of the modelling period. Available [here](./auxiliary-data/population/).
- Monthly births data by country. This information has to be intended as the number of births in the country in each month of the modelling period. Available [here](./auxiliary-data/births/).
- List of countries, available [here](./supporting-files/countries.csv).
- List of weeks in the modelling period, available [here](./supporting-files/isoweeks.csv).

## Submission Format
General guidance for the submission format is provided in the [Wiki](https://github.com/european-modelling-hubs/RespiCompass/wiki/Submission-format). For this specific round, submission file must be saved in [parquet format](https://parquet.apache.org/) and named

```2026_2027_1_RSV-<team>-<model>.parquet```

Where `<team>-<model>` will be specific for each team/model and must match the `team_abbr` and `model_abbr` parameters in the metadata file. Additionally, you should set: 
-  ```round_id = '2026_2027_1_RSV'```
-  ```scenario_id```: TBD
- ```location```: one of the ISO 3166-1 alpha-2 (ISO-2) geocodes for each EU/EEA country. We provide a [geocode file](./supporting-files/countries.csv) to convert between country names and ISO-2 codes.
-  ```target = 'rsv_hospitalisations'```,  ```'administered_doses'```, ```'rsv_infections'```, which denote weekly new RSV hospitalisations, doses administered or infections.
-  ```pop_group``` allowed values are ```'0-2mo_immYes', '0-2mo_immNo', '0-2mo_immTotal', '3-5mo_immYes', '3-5mo_immNo', '3-5mo_immTotal', '6-11mo_immYes', '6-11mo_immNo', '6-11mo_immTotal', '1-4_immYes', '1-4_immNo', '1-4_immTotal', '5-17_immYes', '5-17_immNo', '5-17_immTotal', '18-59_immYes', '18-59_immNo', '18-59_immTotal', '60-64_immYes', '60-64_immNo', '60-64_immTotal', '65-69_immYes', '65-69_immNo', '65-69_immTotal', '70-74_immYes', '70-74_immNo', '70-74_immTotal', '75-79_immYes', '75-79_immNo', '75-79_immTotal', '80+_immYes', '80+_immNo', '80+_immTotal', 'total_immYes', 'total_immNo', 'total_immTotal'```, and ```'undefined'``` (when ```target='administered_doses'```, see below), covering all combinations of considered age groups and immunisation status that are the source population for the weekly incidence. Note that groups ```immYes``` are individuals that were immunised prior to the hospitalisation or infection during the scenario period. When ```target='administered_doses'``` set ```pop_group``` equal to ```'undefined'```.
- ```horizon```: weeks ahead in the projection period, see [here](./supporting-files/isoweeks.csv) for a horizon/week correspondence
- ```target_end_date``` end date of target week, see [here](./supporting-files/isoweeks.csv) for a date/week correspondence
- ```output_type```: we request teams to submit between 100 and 300 individual trajectories for each scenario. For trajectories ```output_type='sample'```.
- ```output_type_id```: '1' to '300' for samples. In cases where “matched” trajectories are used (i.e., trajectories that share the same parameter set across different scenarios), the same ```output_type_id``` should be assigned across those scenarios to maintain consistency.
- ```value```: the value for the given target, location, week, population group and trajectory.

**Note on age groups**: the age groups are defined such that ```'0-2mo'``` includes infants that have between 0 and approximately 89 days of age, ```'3-5mo'``` includes infants that have between 90 and 179 days of age, ```'6-11mo'``` includes infants that have between 180 and 364 days of age.

# Contacts
If you have any question regarding this scenario round do not hesitate to get in touch at [rsv-respicompass@isi.it](mailto:rsv-respicompass@isi.it).


# References
1. Obando-Pacheco P, Justicia-Grande AJ, Rivero-Calle I, Rodríguez-Tenreiro C, Sly P, Ramilo O, et al. Respiratory syncytial virus seasonality: a global overview. J Infect Dis. 2018;217(9):1356-64. Available at: https://academic.oup.com/jid/article/217/9/1356/4823502
2. Fistera D, et al. RSV in adults: clinical spectrum and presentation. 2024.
3. Falsey AR, Walsh EE. Respiratory syncytial virus infection in adults. Clin Microbiol Rev. 2005;18(1):100716.
4. Yoon JG, et al. Clinical characteristics and disease burden of respiratory syncytial virus infection among hospitalized adults. 2020.
5. Osei-Yeboah R, Spreeuwenberg P, Del Riccio M, Fischer TK, Egeskov-Cavling AM, Bøås H, et al. Estimation of the number of respiratory syncytial virus-associated hospitalizations in adults in the European Union. J Infect Dis. 2023;228(11):1539-48. Available at: https://www.ncbi.nlm.nih.gov/pubmed/37246742
6. Del Riccio M, Spreeuwenberg P, Osei-Yeboah R, Johannesen CK, Fernandez LV, Teirlinck AC, et al. Burden of Respiratory Syncytial Virus in the European Union: estimation of RSV-associated hospitalizations in children under 5 years. J Infect Dis. 2023;228(11):1528-38. Available at: https://www.ncbi.nlm.nih.gov/pubmed/37246724
