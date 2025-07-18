# Target Data

### ⚠️⚠️⚠️ Warning
The repository is currently under construction for the 2025/2026 scenario round. All information is not final and subject to change until this message is removed.

This folder contains target data for Round 1 2025/2026 for RSV. In particular, we provide weekly new RSV-associated hospitalisations for each country and age-specific aggregated burden for the period September $1^{st}$ 2025 (2025-W36) to May $31^{st}$ 2026 (2026-W22) in absence of universal RSV immunisation interventions. This data must be used to calibrate models to the baseline ('status-quo') scenario. In other words, in Scenario E, models should aim to reproduce the target data as closely as possible, capturing both the overall seasonal patterns and age-specific contribution to overall burden.

Due to the scarcity of RSV surveillance data in the EU/EEA, we use a combination of cumulative yearly hospitalisation estimates and standardised hospitalisation time-series to obtain age and country-specific weekly hospitalisations accounting for under-reporting. In other words, we synthetically generate weekly RSV hospitalisation data for each country and age-specific burden using robust estimates from the literature. In this sense, the target data is a synthetic proxy of the true hospitalisation burden in absence of intervention and should not be considered as a direct observation nor a prediction for the 2025/2026 RSV season (more details below).

We provide **two files**: 
- `hospitaladmissions.csv`: Total (across age groups) weekly RSV-associated hospitalisations in each country for the period September $1^{st}$ 2025 (2025-W36) to May $31^{st}$ 2026 (2026-W22) in absence of interventions. This file has the following columns: 

    | Column Name | Description |
    |  :-:|  :-: |
    | `country` | Country name |
    | `age_group` | Age group (in this case, always `total`) |
    | `target_end_date` | Date (ISO week, Sunday of the week) |
    | `year_week` | Year and week number (e.g. 2025-W36, this matches the `week` and `year` columns, provided for convenience) |
    | `week` | Week number |
    | `year` | Year |
    | `weekly_rsv_hospitalisations` | Total (across age groups) weekly RSV-associated hospitalisations |

- `hospitalburden_agegroups.csv`: Age-specific aggregated burden of RSV-associated hospitalisations in each country for the period September $1^{st}$ 2025 (2025-W36) to May $31^{st}$ 2026 (2026-W22) in absence of interventions. This file has the following columns: 
    | Column Name | Description |
    |  :-:|  :-: |
    | `country` | Country name |
    | `age_group` | Age group (one of: 0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y) |
    | `start_date` | Start date of the period to which the data refers to ($1^{st}$ September 2025) |
    | `end_date` | End date of the period to which the data refers to ($31^{st}$ May 2026) |
    | `total_rsv_hospitalisations` | Total (across age groups) RSV-associated hospitalisations |

The rationale for producing two separate files is to provide a clear overall seasonal pattern of hospitalisations while allowing flexibility in the age-specific profiles, with total age-specific burdens still available and shared across models. Different age groups may exhibit distinct seasonal trends due to variations in susceptibility to RSV and assumptions about inter-age-group contact patterns. In the absence of detailed age-specific seasonal data, it is challenging to generate plausible age-specific hospitalisation curves that align with the overall seasonal pattern and are compatible with most modelling frameworks. Therefore, we opted to provide the total burden by age group and the overall seasonal trend as separate inputs.


## EU/EEA RSV Synthetic Data Generation
Calibration of RSV transmission models for assessing national immunisation intervention strategies requires age- and country-specific incidence data over time. However, the sensitivity and specificity of national RSV surveillance systems in the EU/EEA is highly heterogeneous, with underreporting known to be a major limitation [1,2]. Estimates of cumulative yearly RSV hospitalisation burden in Europe based on large-scale hospital and virological data are available through studies like [3-5] which provide comprehensive estimates of cumulative yearly RSV hospitalization burden. In turn [6] published average RSV reported hospitalisation time series for Europe. Here, we use a method to combine cumulative hospitalisation estimates and standardised hospitalisation time-series to obtain age and country-specific weekly hospitalisation incidence accounting for under-reporting. 

Our proposed data generation approach works as follows.

**Inputs:** 
| Input | Description | Source |
|  :-:|  :-: | :-: |
| $h^{c,a}$ | Annual estimated (median) RSV-hospitalizations per 1,000 in age group $a$ and country $c$ | [3] (infants), [4] (adults)* |
| $h_{ref}(t)$ | RSV-hospitalizations observed in week $t$ of a reference season | [6] |
| $P^{c,a}$ | Recent population data for country $c$ and age group $a$ | [7] |

$^{*}$ **Note**: these two studies provide country-specific estimates of RSV-hospitalizations per 1,000 population for the following age groups: 0-2mo, 3-5mo, 6-11mo, 1-2y, 3-4y, 18-64y, 65-74y, 75-84y, 85+y. We apply the algorithm described below to obtain overall annual burden for these age groups and then we aggregate them to the age groups requested for this scenario round. Additionally, for the missing 5-17y group, we use the 18-64yo age group hospitalisation rate estimates.

**Algorithm:** 

For each country $c$: 
1. Compute total annual RSV-hospitalizations by country $c$ and age group $a$ (rounded to the nearest integer): 
    $$H^{c,a} = \lfloor (h^{c,a} /1,000\times P^{c,a}) \rfloor$$
2. Total annual RSV-hospitalizations are the sum of RSV-hospitalizations in all age groups for a given country $c$: 
    $$H^{c}=\sum_{a}H^{c,a}$$
3. For each week $t$, compute the share of RSV-hospitalizations observed in week $t$ of the reference season: 
        $$\psi(t)=\frac{h_{ref}(t)}{\sum_{t'}h_{ref}(t')}$$
4. Compute weekly RSV-hospitalizations for each week $t$ for country $c$ considering a multinomial distribution: 
    $$(H^c(t_1), H^c(t_2) \ldots, H^c(t_T)) \sim \text{Multinomial}(H^c, (\psi(t_1), \psi(t_2), \ldots, \psi(t_T)))$$


This algorithm outputs: 
- $\mathbf{H}^c_t = (H^c(t_1), H^c(t_2) \ldots, H^c(t_n))$, which consists of total weekly RSV-associated hospitalizations for a given country $c$ for all weeks $t$. This information is provided in the `hospitaladmissions.csv` file.

- $\mathbf{H}^{c,a} = (H^{c,a_1}, H^{c,a_2}, \ldots, H^{c,a_n})$, which consists of aggregated RSV-associated hospitalizations per each age group for a given country $c$. This information is provided in the `hospitalburden_agegroups.csv` file.


# Contacts
If you have any question regarding this scenario round do not hesitate to get in touch at [rsv-respicompass@isi.it](mailto:rsv-respicompass@isi.it).


# References
1. Presser LD, van den Akker WM, Meijer A. Respiratory syncytial virus European laboratory network 2022 survey: need for harmonization and enhanced molecular surveillance. The Journal of Infectious Diseases. 2024 Mar 15;229(Supplement_1):S34-9. Available at: https://academic.oup.com/jid/article/229/Supplement_1/S34/7242218
2. Egeskov-Cavling, Amanda Marie, et al. Underreporting and misclassification of respiratory syncytial virus–coded hospitalization among adults in Denmark between 2015–2016 and 2017–2018. The Journal of infectious diseases 229.Supplement_1 (2024): S78-S83. Available at:https://academic.oup.com/jid/article/229/Supplement_1/S78/7281854
3. Del Riccio M, Spreeuwenberg P, Osei-Yeboah R, Johannesen CK, Fernandez LV, Teirlinck AC, et al. Burden of Respiratory Syncytial Virus in the European Union: estimation of RSV-associated hospitalizations in children under 5 years. J Infect Dis. 2023 2023/11/28;228(11):1528-38. Available at: https://www.ncbi.nlm.nih.gov/pubmed/37246724
4. Osei-Yeboah R, Spreeuwenberg P, Del Riccio M, Fischer TK, Egeskov-Cavling AM, Bøås H, et al. Estimation of the number of respiratory syncytial virus-associated hospitalizations in adults in the European Union. J Infect Dis. 2023 2023/11/28;228(11):1539-48. Available at: https://www.ncbi.nlm.nih.gov/pubmed/37246742
5. Li X, Hodgson D, Flaig J, Kieffer A, Herring WL, Beyhaghi H, Willem L, Jit M, Bilcke J, Beutels P, REspiratory Syncytial virus Consortium in EUrope (RESCEU) Investigators. Cost-effectiveness of respiratory syncytial virus preventive interventions in children: a model comparison study. Value in health. 2023 Apr 1;26(4):508-18. Available at: https://www.sciencedirect.com/science/article/pii/S1098301522047465
6. Johannesen CK, van Wijhe M, Tong S, Fernández LV, Heikkinen T, van Boven M, Wang X, Bøås H, Li Y, Campbell H, Paget J. Age-specific estimates of respiratory syncytial virus-associated hospitalizations in 6 European countries: a time series analysis. The Journal of infectious diseases. 2022 Aug 1;226(Supplement_1):S29-37. Available at: https://academic.oup.com/jid/article/226/Supplement_1/S29/6617433
7. Eurostat. Population by age and sex. 2025. Available at: https://ec.europa.eu/eurostat/databrowser/product/page/DEMO_PJAN. DOI: https://doi.org/10.2908/DEMO_PJAN
