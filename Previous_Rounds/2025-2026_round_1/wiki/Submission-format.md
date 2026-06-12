Projections should be stored as a [parquet file](https://parquet.apache.org/) in your `model-output/<team>-<model>` folder.

The parquet file must use a standardised file name, and contain specific variable names and values which identify the projections you are submitting. The automatic check validates both the filename and file contents to ensure the file is correct.

## File name
Each projection file within the subdirectory should have the following name format:

`<round_id>-<team>-<model>.parquet`

The `<round_id>` is defined uniquely for each submission round and disease. It is composed by the `season_cycle`, identifying the season and the submission cycle, and the `disease` indicator.
The `<team>` and `<model>` in this file name must match the name of the `model-output` directory this file is in (and correspond to the `team_abbr` and `model_abbr` parameters in the metadata file). E.g. `model-output/ISI-TestModel/2025_2026_1_RSV-ISI-TestModel.parquet`

## File format
### Required variables
The parquet file must be contain only the following columns (in any order). No additional columns are allowed.

| column | data type | description |
| -------- | -------- | ------- |
| [`round_id`](#round_id) | string | The id of the submission round, '2025_2026_1_RSV', composed by the season cycle ('2025_2026_1') plus the disease ('RSV'). Will be defined for each round. |
| [`scenario_id`](#scenario_id) | string | Id of the scenario as described in the round specifications (e.g. 'A', 'B', ...).|
| [`target`](#target) | string | One of the targets defined/allowed for the round. |
| [`location`](#target_horizon) | string | One of the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (ISO-2) geocodes for the European country. We provide a [geocode file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/countries.csv) to convert between country names and ISO-2 codes or, if using R, you can use the [countrycode package](https://cran.r-project.org/web/packages/countrycode/index.html). |
| [`pop_group`](#pop_group) | string | The age bin, or another population breakdown identifier, as defined in the round specs. |
| [`horizon`](#horizon) | integer | Values in the horizon column must be an integer indicating the weeks ahead from the origin date corresponding to the projected value. Each week starts on Monday and ends on Sunday. For more details check the [template file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/supporting-files/isoweeks.csv) for CSV files converting between dates and ISO weeks.|
| [`target_end_date`](#target_end_date) | date | Target date corresponding to the projected value. Values must be a date in the format `YYYY-MM-DD`. |
| [`output_type`](#output_type) | string | output_type value for trajectories  is fixed at 'sample'. |
| [`output_type_id`](#output_type_id) | string | Shall be a value from '1' to '300' identifying the stochastic run for sample data. |
| [`value`](#value) | double | The value of the prediction for the given target. |

(*): The origin date of the scenario simulations will be defined for each round and season_cycle and mentioned explicitly in the github Wiki documentation. 

## Parquet file format
The "arrow" library can be used to read/write the parquet files in [R](https://arrow.apache.org/docs/r/index.html) and in [Python](https://arrow.apache.org/docs/python/parquet.html), where "pandas" library can be used as well.

For example, in R you can load "arrow" and then:
```R
library("arrow")

file_name <- ”model-output/team-model/round_id-team-model.parquet”

# To read "parquet" file format
arrow::read_parquet(filename)

# To write "parquet" file format
arrow::write_parquet(df, file_name)

```

The following code does the same but using Python and "pandas":
```Python
import pandas as pd

file_name = 'model-output/team-model/round_id-team-model.parquet'

# To read "parquet" file format:
df = pd.read_parquet(file_name)

# Write "parquet" file format
df.to_parquet(file_name)

```

<!-- You can consult an [example model output parquet file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/model-output/ISI-TestModel/2025_2026_1_RSV-ISI-TestModel.parquet) for further guidance. -->

