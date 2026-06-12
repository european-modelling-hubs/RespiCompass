Scenario projections has to be submitted using pull requests from a forked version of this repository. This will trigger all the validation checks to ensure a successful acquisition of the projections.

1. *Only for the first submission.* Go to the repository [`RespiCompass`](https://github.com/european-modelling-hubs/RespiCompass) on GitHub and click on `Fork` button to create your personal copy of the repository

2. Sync your repository clicking the `Sync fork` button (in the root page of the repository). 

3. a. *Only for the first submission.* Navigate to the `model-output` folder (where all the projections are stored), click on the `AddFile / Upload files` button in the upper-right corner and drag and drop your submission folder (or chose it using the file browser); the folder must be named in the format <team>-<model> (where team and model correspond to the `team_abbr` and `model_abbr` fields of the metadata file).

	b. *Subsequent submissions.* Navigate to your *<team>-<model>* submission folder under `model-output` and click on the `AddFile / Upload files` button in the upper-right corner; then drag and drop your files (or choose it using the file browser).

4. Give the commit a meaningful name using: `team_abbr` `model_abbr` Metadata and/or `round_id`, based on submission type (e.g. “TeamX ModelY 2025_2026_1_RSV”), select "Commit directly to the main branch" option and click `Commit changes` to commit changes to your local fork.

	*Since your changes are uploaded to the local fork, you need to open a Pull Request.*

5. Move to your fork main folder and click on `Contribute / Open pull request` button.

6. Make sure that the `base repository` is the main repository and the `head repository` is your fork.

7. Enter as title of the PR your team name, model name and round_id, and then click on `Create pull request` button.

8. Wait for validation and merge.

*For subsequent submissions repeat from point 2*
