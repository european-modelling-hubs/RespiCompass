Scenario projections has to be submitted using pull requests from a forked version of this repository. This will trigger all the validation checks to ensure a successful acquisition of the projections. Using the command line requires some technical expertise and some knowledge of the git framework. If you are not confident you shall [submit using GitHub Website](Submitting-using-GitHub-Website).

1. Install the [GitHub cli](https://cli.github.com/).

2. Authenticate your user using the GitHub cli:
 
	*gh auth login*

	To do so you need first to create a *Personal access token* (info [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)) with at least the _repo_, _workflow_ and _admin:org_ scopes enabled.

3. [Fork and clone](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) the `RespiCompass` repository using the  GitHub cli:
	
	*gh repo fork european-modelling-hubs/RespiCompass --clone=true*
 
4. Set default repository to use when querying the GitHub API for local clone to `RespiCompass` using:  

	*gh repo set-default european-modelling-hubs/RespiCompass*

5. Be sure your local fork is up to date with the original repo, syncing it:
	
	*git checkout main*

	*gh repo sync <your_github_handle>/RespiCompass -b main*
	
	*git pull*

6. Create a new branch for the submission and switch to it:

	*git checkout -b <submit_branch>*

	(The name of the branch should be new, for example "submit_branch_YYYYMMDD").

7. Navigate to the `model-output` folder (where all the projections are stored).

	**ONLY BEFORE THE FIRST SUBMISSION**: Create and name your own folder in the format `<team>-<model>` (where team and model correspond to the `team_abbr` and `model_abbr` fields of the metadata file). 

8. Copy your projections/changes file to your projections folder (the `<team>-<model>` folder above). 

9. Commit your changes via the standard git commands:
	
	*git add --all*
	
	*git commit -m "Commit comment"*

10. Submit a [pull request](https://help.github.com/en/enterprise/2.16/user/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) to the main branch of the [RespiCompass](https://github.com/european-modelling-hubs/RespiCompass) repository. Please use your team name, model name and and round_id as the *title* of the pull request.

	*gh pr create*

11. Wait for validation and merge.

**FOR SUBSEQUENT SUBMISSIONS REPEAT FROM POINT 5**. 
