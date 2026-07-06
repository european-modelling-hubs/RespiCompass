# Auxiliary Data

This folder provides auxiliary data to support model development and calibration for RespiCompass Round-1 of 2026/2027 RSV season.

## Population data 

See dedicated [README](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/population) for more information.


## Births data 

See dedicated [README](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/births) for more information.


## Mortality data

See dedicated [README](https://github.com/european-modelling-hubs/RespiCompass/tree/main/auxiliary-data/mortality) for more information.


## Additional information 
We provide below additional information and links that may be useful for model development, calibration and projection.

### Demographic effects
Eurostat provides data on [mortality rates](https://ec.europa.eu/eurostat/databrowser/view/demo_magec__custom_17436898/default/table?lang=en) (dataset DOI: https://doi.org/10.2908/DEMO_MAGEC) by single year of age and sex by country of occurrence.


### Age of mothers at birth in EU/EEA countries
We refer teams to the [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/demo_fagec__custom_17395850/default/table) (dataset DOI: https://doi.org/10.2908/DEMO_FAGEC) data on age of mothers at birth in EU/EEA countries.


### Age-specific contact patterns 

- [The CoMix Study data](https://socialcontactdata.org/data/)
- Synthetic contact matrices from [Mistry et al, 2021](https://github.com/mobs-lab/mixing-patterns), [Prem et al, 2021](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009098), [Prem et al, 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005697)

To load the contact matrices using the R programming language, you can use the `socialmixr` package, following the [detailed instructions for installation and usage](https://cran.r-project.org/web/packages/socialmixr/vignettes/socialmixr.html). In Python, you can refer to the [`epydemix`](https://github.com/epistorm/epydemix) package, see here for [detailed instructions](https://github.com/epistorm/epydemix-data/) and [tutorials](https://github.com/epistorm/epydemix/blob/main/tutorials/2_Modeling_with_Population_Data.ipynb).

# Contacts
If you have any question regarding this scenario round do not hesitate to get in touch at [rsv-respicompass@isi.it](mailto:rsv-respicompass@isi.it).
