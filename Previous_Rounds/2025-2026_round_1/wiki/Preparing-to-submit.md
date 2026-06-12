Below we explain the steps needed to submit your first scenario projections to this hub. 

We rely on GitHub to store and interact with projections. To submit projections, you will need a free GitHub account; if you don't have one you can use the "Sign up" link at the top-right of the page. 

Broadly, the steps to submit are:

1. [Fork](https://guides.github.com/activities/forking/) this repository (called `RespiCompass`)
    - Use the `Fork` button at the top right of the main page of the repository
    - (optional) In case you want to use the CLI and keep your fork synchronized with the main repository, [configure a remote](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork) and [sync](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) your fork


2. Create a [metadata file](Metadata), including information about the team and methods. The metadata file should be placed in the folder [`model-metadata`](https://github.com/european-modelling-hubs/RespiCompass/tree/main/model-metadata) and named:

    **`<team>-<model>.yml`**

    Where:
    
    * `<team>` is the team name (corresponding to the field `team_abbr` of the metadata file, see below) 
    * `<model>` is the name of your model (corresponding to the field `model_abbr` of the metadata file, see below) 
	
    Both `<team>` and `<model>` must be less than 15 characters and can include only uppercase or lowercase letters, digits, the `_` and the `+` sign (e.g.: `model-metadata/ISI-TestModel.yml`)


3. Create a new sub-directory for your team. Each team stores their projections in a separate folder within the [`model-output`](https://github.com/european-modelling-hubs/RespiCompass/tree/main/model-output) folder of this repository.
	Before submitting your first projection, please create and name your own folder in the format:
    
    **`<team>-<model>`**
    
	Where:
    
	* `<team>` is the team name (corresponding to the field `team_abbr` of the metadata file, see below) 
	* `<model>` is the name of your model (corresponding to the field `model_abbr` of the metadata file, see below) 
	
    Both `<team>` and `<model>` must be less than 15 characters and can include only uppercase or lowercase letters, digits, the `_` and the `+` sign (e.g.: `model-output/ISI-TestModel/`).

    If submitting multiple models, please create a `<team>-<model>` folder for each one


4. Submit metadata and/or projections by [[creating a pull request | Create a Pull Request]]

It is possible to submit the projections in two different ways, depending on personal preferences and technical expertise: the gitHub Web interface and the command line.
The steps above are explained in more detail in the following pages, providing instructions for: 

* [submitting via the website](Submitting-using-GitHub-Website)
* [submitting via the command line](Submitting-using-GitHub-Command-Line)

If you are new to GitHub and pull request, here are some helpful beginner [guides to Github](https://makeapullrequest.com/).
