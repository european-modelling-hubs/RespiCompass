Each model is required to have metadata stored in a text file. Please read the instructions here carefully before preparing the first submission, as this will fail if the metadata file is not supplied, or not supplied in the right format.

The text file should be named `<team>-<model>.yml` and saved in the [`model-metadata/` directory](https://github.com/european-modelling-hubs/respicompass/tree/main/model-metadata). Each of `<team>` and `<model>` are text strings that are less than 15 alphanumeric characters, and can't include a hyphen or whitespace. They must correspond to the `team_abbr` and `model_abbr` parameters listed below.

This `<team>-<model>.yml` file shall be written in [yaml format](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html), copying the below structure. This document describes each of the parameters (keys) in the yaml file. Please order the variables in this order. You can consult an [example metadata file](https://github.com/european-modelling-hubs/RespiCompass/blob/main/model-metadata/ISI-TestModel.yml) for further guidance. Each line should contain one `key: value` pair.

Upon first submission, a series of checks will be run on the Metadata file, and an error thrown if any of the checks fails - a common problem, for example, is that the text contains a colon (`:`) - if that is the case, you may instead put quotation marks (`"`) around the entry. If you are having trouble getting the metadata to pass the checks, please do not hesitate to get in touch with us [European.Modelling.Hub@ecdc.europa.eu](mailto:European.Modelling.Hub@ecdc.europa.eu). For future submission, the metadata file only needs to be changed if there is a change in the model information (e.g., additional input data is being used).

## Required parameters

### team_name
The name of your team, must be at most 50 characters long.

### model_name
The name of your model, must be at most 50 characters long.

### team_abbr 
The abbreviated name of the the team submitting the model. This is for uniquely identifying the team 
in our system, and should be equal to the first part of the name of your sub-directory in the 
`model-output` folder (the part before the hyphen `-`).
This should be a short name for the team that is less than 15 characters, and  can include only uppercase or lowercase letters, digits, the `_` and the `+` sign. Examples of a valid model_abbr string are `Ecdc` or `ISI`.

### model_abbr
The abbreviated name of the the model. This is for uniquely identifying the model in our system, and should be equal to the second part of the name of your sub-directory 
in the `model-output` folder (the part after the hyphen `-`).
This should be a short name for the model that is less than 15 characters, and  can include only uppercase or lowercase letters, digits, the `_` and the `+` sign. 
Examples of a valid model_abbr string are `TestModel` or `SvEIR`.

### model_contributors

A list of all individuals involved in the predicting effort and their affiliations. All contributors need to provide name, affiliation, and email. All email addresses provided will be added to an email distribution list for model contributors.

The syntax of this field should be

```
model_contributors:
  - name: Contributor 1
    affiliation: Affiliation 1
    email: user1@example.com
  - name: Contributor 2
    affiliation: Affiliation 2
    email: user2@example.com
```

For each contributor, you can also add the optional `twitter` and `orcid` fields.

### methods

A brief description of your methodology that is less than 200 characters.

### data_inputs

A description of the data sources used to inform the model. For example, sources might include epidemiological, demographic, and behavioural data.


## Optional parameters

### license

By default, projections are released under a CC-BY 4.0 license. If you would like to release your projections under a different license, please specify a [standard license](https://github.com/cdcepi/Flusight-forecast-data/blob/master/accepted-licenses.csv) in the license field of your metadata file.

### team\_model\_designation

Upon initial submission this field should be one of “primary”, “proposed” or “other”. For teams submitting only one model, this should be “primary”. For each team, only one model can be designated as “primary”.

* *Primary* means the model will be scored in evaluations, eligible for inclusion in the ensemble, and visualized.

* *Proposed* means the team would like the model to be considered as a "secondary" model rather than an "other" model.
  * The Hub team will determine whether the model's methodology is distinct enough that the model should be included in the analysis, in which case the model will get the "secondary" designation.
  * If the methodology is not distinct enough, e.g. it differs from the primary model by setting certain parameters to specific values, then the model will be designated as "other".

* *Secondary* means that model is eligible for inclusion in the analysis and evaluations.

* *Other* means the projections will not be visualized or included in the analysis.

### team_funding

Like an acknowledgement in a manuscript, you can acknowledge funding here.

### website_url

A url to a website, report, GitHub repository, or publication that contains additional information about your model.

### citation

A url (doi link preferred) to an extended description of your model,
e.g. blog post, website, preprint, or peer-reviewed manuscript.

### methods_long

An extended description of the methods used in the model.

If the model is modified, this field can be used to provide:
* date of modification
* description of the change


***

**Note**: When you upload the model meta-data file, ECDC will collect the personal data that you provide (your name and email) and include this data in an email distributor and a Discussion forum, as a mean of communication between ECDC and you. You can unsubscribe at any time, and ECDC will then delete your personal data.