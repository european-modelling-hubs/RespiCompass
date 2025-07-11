# Target Data

### ⚠️⚠️⚠️ Warning
The repository is currently under construction for the 2025/2026 scenario round. All information is not final and subject to change until this message is removed.

This folder contains target data for Round 1 2025/2026 for RSV. In particular, we provide weekly new RSV-associated hospitalisations for each country and age-specific aggregated burden for the period September 2025 to March 2026 in absence of interventions. This data must be used to calibrate models to the baseline scenario. In other words, in Scenario E, models should aim to reproduce the target data as closely as possible, capturing both the overall seasonal patterns and age-specific burdens.

Due to the scarcity of RSV surveillance data in the EU/EEA, we use a combination of cumulative yearly hospitalisation estimates and standardised hospitalisation time-series to obtain age and country-specific weekly hospitalisations accounting for under-reporting. In other words, we synthetically generate weekly hospitalisation data for each country and age-specific burden using robust estimates from the literature. In this sense, the target data is a synthetic best-guess estimate of the true hospitalisation burden in absence of intervention and should not be considered as a direct observation nor a prediction for the 2025/2026 RSV season.

We provide **two files**: 
- `hospitaladmissions.csv`: Total (across age groups) weekly RSV-associated hospitalisations in each country for the period September 2025 to March 2026 in absence of interventions. This file has the following columns: 

    | Column Name | Description |
    |  :-:|  :-: |
    | `country` | Country name |
    | `age_group` | Age group (in this case, always `total`) |
    | `date` | Date (ISO week, Monday of the week) |
    | `year_week` | Year and week number (e.g. 2025-W36, this matches the `week` and `year` columns, provided for convenience) |
    | `week` | Week number |
    | `year` | Year |
    | `weekly_rsv_hospitalisations` | Total (across age groups) weekly RSV-associated hospitalisations |

- `hospitalburden_agegroups.csv`: Age-specific aggregated burden of RSV-associated hospitalisations in each country for the period September 2025 to March 2026 in absence of interventions. This file has the following columns: 
    | Column Name | Description |
    |  :-:|  :-: |
    | `country` | Country name |
    | `age_group` | Age group (one of: 0-2mo, 3-5mo, 6-11mo, 1-4y, 5-64y, 65+y) |
    | `start_date` | Start date of the period to which the data refers to ($1^{st}$ September 2025) |
    | `end_date` | End date of the period to which the data refers to ($27^{th}$ April 2026) |
    | `total_rsv_hospitalisations` | Total (across age groups) RSV-associated hospitalisations |

The rationale for producing two separate files is to provide a clear overall seasonal pattern of hospitalisations while allowing flexibility in the age-specific profiles, with total age-specific burdens still available and shared across models. Different age groups may exhibit distinct seasonal trends due to variations in susceptibility to RSV and assumptions about inter-age-group contact patterns. In the absence of detailed age-specific seasonal data, it is challenging to generate plausible age-specific hospitalisation curves that align with the overall seasonal pattern and are compatible with most modelling frameworks. Therefore, we opted to provide the total burden by age group and the overall seasonal trend as separate inputs.


## EU/EEA RSV Synthetic Data Generation
Calibration of dynamic RSV models for assessing national immunisation intervention strategies requires age- and country-specific incidence data over time. However, the sensitivity and specificity of national RSV surveillance systems in the EU/EEA is highly heterogeneous, with underreporting known to be a major limitation ([Presser et al. 2023](https://doi.org/10.1093/infdis/jiad341), [Egeskov-Cavling et al. 2023](https://doi.org/10.1093/infdis/jiad382)). Estimates of cumulative yearly RSV hospitalisation burden in Europe based on large-scale hospital and virological data are available through studies like [Del Riccio et al. 2023](https://doi.org/10.1093/infdis/jiad188), [Osei-Yeboah et al. 2023](https://doi.org/10.1093/infdis/jiad189), and [Li et al. 2022](https://pubmed.ncbi.nlm.nih.gov/36442831/) which provide comprehensive estimates of cumulative yearly RSV hospitalization burden. In turn, [Johannesen et al. 2022](https://academic.oup.com/jid/article/226/Supplement_1/S29/6617433?login=true) published average RSV reported hospitalisation time series for Europe. Here, we use a method to combine cumulative hospitalisation estimates and standardised hospitalisation time-series to obtain age and country-specific weekly hospitalisation incidence accounting for under-reporting. 

Our proposed data generation approach works as follows.

**Inputs:** 
| Input | Description | Source |
|  :-:|  :-: | :-: |
| $h^{c,a}$ | Annual estimated (median) RSV-hospitalizations per 1,000 in age group $a$ and country $c$ | [Del Riccio et al. 2023](https://doi.org/10.1093/infdis/jiad188) (infants), [Osei-Yeboah et al. 2023](https://doi.org/10.1093/infdis/jiad189) (adults)$^{*}$ |
| $h_{ref}(t)$ | RSV-hospitalizations observed in week $t$ of a reference season | [Johannesen et al. 2022](https://academic.oup.com/jid/article/226/Supplement_1/S29/6617433?login=true) |
| $P^{c,a}$ | Recent population data for country $c$ and age group $a$ | [Eurostat](https://doi.org/10.2908/DEMO_PJAN) |

$^{*}$ **Note**: these two studies provide country-specific estimates of RSV-hospitalizations per 1,000 population for the following age groups: 0-2mo, 3-5mo, 6-11mo, 1-2y, 3-4y, 18-64y, 65-74y, 75-84y, 85+y. We apply the algorithm described below to obtain overall annual burden for these age groups and then we aggregate them to the age groups requested for this scenario round. Additionally, for the missing 5-17y group, we use the 18-64yo age group hospitalisation rate estimates.

**Algorithm:** 

For each country $c$ and age group $a$: 
1. Compute total annual RSV-hospitalizations by country $c$ and age group $a$: 
    $$H^{c,a} = h^{c,a} /1,000\times P^{c,a}$$
2. Total annual RSV-hospitalizations are the sum of RSV-hospitalizations in all age groups for a given country $c$: 
    $$H^{c}=\sum_{a}H^{c,a}$$
3. For each week $t$: 
    - Compute the share of RSV-hospitalizations observed in week $t$ of the reference season: 
        $$\psi(t)=h_{ref}(t) / \sum_{t'}h_{ref}(t')$$
    - Compute total RSV-hospitalizations in week $t$ for country $c$: 
        $$H^{c}(t)=\psi(t) H^{c}$$

**Output:** 

This algorithm outputs: 
- $H^{c}(t)$, which consists of total weekly RSV-associated hospitalizations for a given country $c$ for all weeks $t$. This information is provided in the `hospitaladmissions.csv` file.

- $H^{c,a}$, which consists of aggregated RSV-associated hospitalizations per each age group for a given country $c$. This information is provided in the `hospitalburden_agegroups.csv` file.





