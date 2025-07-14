# Auxiliary Data

### ⚠️⚠️⚠️ Warning
The repository is currently under construction for the 2025/2026 scenario round. All information is not final and subject to change until this message is removed.

This folder provides auxiliary data to support models development and calibration for RespiCompass Round-1 of 2025/2026 RSV season.

## Population data 

See dedicated [README](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/population) for more information.


## Births data 

See dedicated [README](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/births) for more information.


## Waning of immunity 

See dedicated [README](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/waning) for more information.


## Additional information 
We provide below additional information and links that may be useful for models development, calibration and projection.


### Effectiveness and efficacy of la-mAbs and MV
Teams may model additional effects of la-mAbs and MV at their discretion. For example, this could include protection against infection, both for newborns and mothers in the case of MV, and for newborns in the case of la-mAbs. **At a minimum, we recommend including these protective effects against infection as part of the intervention's impact.**

To support this, we provide the following list of references that may be useful for teams: 

#### la-mAbs

| Source | Endpoint | Efficacy/Effectiveness | Notes | 
|--------|----------|---------------|-------|
|   [Hammitt et al., 2024](https://www.nejm.org/doi/full/10.1056/NEJMoa2110275)     | Medically attended RSV-associated LRTI | 74.5% (95% CI: 49.6-87.1%) | Phase 3 clinical trial |
|  [Xu et al., 2025](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2831181)     | Medically attended RSV infections  | 68.4% (95% CI: 50.3-80.8%) | Test-negative case-control study utilizing inpatient, outpatient, and emergency department data from the Yale New Haven Health System |
|      | Outpatient visits  | 61.6% (95% CI: 35.6-78.6%) | "|
|      | Severe RSV disease  | 84.6% (95% CI: 58.7-95.6%) | " |
|      | RSV infection (2 weeks post-immunization)  | 79.3% (95% CI: 63.4-90.6%) | " |
|      | RSV infection (14 weeks post-immunization)  | 54.8% (95% CI: 16.3-74.7%) | " |
|  [Lefferts et al., 2024](https://www.cdc.gov/mmwr/volumes/73/wr/mm7345a1.htm)     | Medically attended RSV illness  | 76% (95% CI: 42–90%) | Test-negative case-control study utilizing Alaska’s Yukon-Kuskokwim Delta region data |
| [Sumsuzzman et al., 2025](https://www.sciencedirect.com/science/article/abs/pii/S2352464225000938) | RSV-related LRTI incidence |  75.0% (95% CI: 67.0–81.0%) | Systematic review and meta-analysis considering 32 cohort and case-control studies from five countries (France, Italy, Luxembourg, Spain, and the USA)|
|  | RSV-related ICU admission |  81.0% (95% CI: 71.0–88.0%) | "|
| [Li et al., 2025](https://kce.fgov.be/sites/default/files/2025-06/KCE_402_RSV_Infections_Belgian_Infants_Report.pdf) | Medically-attended RSV-LRTI (clinical trials) | 75% (95%CI: 64-82) | Systematic review and meta-analysis |
| [Hodgson et al., 2024](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(23)00248-X/fulltext) |  Milder health outcomes   | ~90% | Modeled values immediately after vaccination, see Figure 2 |
|  |  More severe outcomes   | ~90% | Modeled values immediately after vaccination, see Figure 2 |


#### MV (neonates)

| Source | Endpoint | Efficacy/Effectiveness | Notes | 
|--------|----------|---------------|-------|
| [Mapindra et al., 2024](https://karger.com/neo/article/121/3/271/894569/Respiratory-Syncytial-Virus-Maternal-Vaccination) | Medically attended RSV LRTI | 53% (95% CI: 2-77%) | Systematic review and meta-analysis considering 6 randomized clinical trials | 
| [Dieussaert et al., 2024](https://www.nejm.org/doi/10.1056/NEJMoa2305478?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed) | Medically assessed RSV-associated LRTI | 65.5% (95% CI: 37.5-82.0%) | Phase 3 clinical trial. **Enrollment in this trial was stopped early because of safety concerns** |
|  | Severe medically assessed RSV-associated LRTI | 69.0% (95% CI: 33-87.6%) | "  |
| [Kampmann et al., 2023](https://www.nejm.org/doi/10.1056/NEJMoa2216480) | Medically attended severe LRTI (90 days after birth) | 81.8% (99.5% CI: 40.6-96.3%)| Phase 3 clinical trial. | 
|  | Medically attended RSV-associated LRTI (90 days after birth) | 57.1% (99.5% CI: 14.7-79.8%)| " | 
| [Hodgson et al., 2024](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(23)00248-X/fulltext) |   Milder health outcomes   | ~60% | Modeled values immediately after vaccination, see Figure 2 |
|  |  More severe outcomes     | ~80% | Modeled values immediately after vaccination, see Figure 2 |

---
#### MV (pregnant women)
| Source | Endpoint | Efficacy/Effectiveness | Notes | 
|--------|----------|---------------|-------|
| [Papi et al., 2023](https://www.nejm.org/doi/pdf/10.1056/NEJMoa2209604) | RSV-related LRTI | 82.6% (95% CI: 57.9-94.1%) | Phase 3 trial of RSVPreF3 candidate vaccine in adults 60+ |
|  |  Severe RSV-related LRTI | 94.1% (95% CI: 62.4-99.9%) | " |
|  |  RSV-related acute respiratory infection | 71.7% (95% CI: 56.2-82.3%) | " |
| [Hodgson et al., 2024](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(23)00248-X/fulltext) |   Milder health outcomes    | ~80% | Modeled values immediately after vaccination, see Figure 2 |
|  |  More severe outcomes    | ~90% | Modeled values immediately after vaccination, see Figure 2 |









### Age of mothers at birth in EU/EEA countries
We refer teams to the [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/demo_fagec__custom_17395850/default/table) (dataset DOI: https://doi.org/10.2908/DEMO_FAGEC) data on age of mothers at birth in EU/EEA countries.


### Age-specific contact patterns 

- [The CoMix Study data](https://socialcontactdata.org/data/)
- Synthetic contact matrices from [Mistry et al, 2021](https://github.com/mobs-lab/mixing-patterns), [Prem et al, 2021](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009098), [Prem et al, 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005697)

To load the contact matrices using the R programming language, you can use the `socialmixr` package, following the [detailed instructions for installation and usage](https://cran.r-project.org/web/packages/socialmixr/vignettes/socialmixr.html). In Python, you can refer to the [`epydemix`](https://github.com/epistorm/epydemix) package, see here for [detailed instructions](https://github.com/epistorm/epydemix-data/) and [tutorials](https://github.com/epistorm/epydemix/blob/main/tutorials/2_Modeling_with_Population_Data.ipynb).
