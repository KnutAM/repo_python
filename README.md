# repo_python
Template repository for python projects



## Setup environment

The goal of this section is to create a requirements.txt file such that other users can easily use the package.

### Using conda

| Action					       | Command 					  |
| ---------------------------------|------------------------------|
| Create a new, clean, environment | `conda create -n <env_name>` |
| Activate the environment 		   | `conda activate <env_name>`  |
| Install pip 					   | `conda install pip`          |
| Install packages required for the package to work | `conda install <required_package>`|
| Write requirements.txt | `pip freeze > requirements.txt`|
| Alternative (not sure yet what is best) | `pip list --format=freeze > requirements.txt`|

Note that the first option for writing to `requirements.txt` produce output which seems strange, but seems to follow  [PEP610](https://www.python.org/dev/peps/pep-0610/). 

#### End user instructions for installing environment using conda
**NOTE**: Not tested
| Action					       | Command 					  |
| ---------------------------------|------------------------------|
| Create a new, clean, environment | `conda create -n <env_name>` |
| Activate the environment 	       | `conda activate <env_name>`  |
| Install pip                      | `conda install pip`          |
| Install requirements             | `pip install -r requirements.txt`|
