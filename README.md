# Template for python repositories
## Initial modifications for a new project

### Installation

In order for users and other developers to work with the package, it is vital that the dependencies are documented properly. Furthermore, this is also required for continuous integration and testing. 

1. Modify the file `setup.py` by updating at least the fields containing words enclosed in angle brackets, e.g. `<package_name>`. 

2. Add minimal requirements (i.e. packages that are imported in your code) to `requirements.txt`. New line for each package, and package specifications can be e.g. 
   - `numpy>=1.0`
   - `scipy`

### Documentation (Sphinx)

Documentation using sphinx allows automatic documentation using docstrings in the code. First, set it up to work locally. For open source projects this can be published to ReadTheDocs. Another alternative is using the GitHub pages. 

#### Local

#### ReadTheDocs

#### GitHub Pages

### Testing

Unit testing can be setup so that it can be run locally. However, the real power and visibility comes when this is run each time the code is pushed to ensure that it works as intended and that nothing has been broken. First, `pytest` is used to create simple tests. Then, `TravisCI` is used to get continuous testing on each push. Finally, code coverage is analyzed. 

#### pytest

#### Automatic testing using TravisCI

#### Coverage analysis using coverage.io

# NOTES

Difference between requirements.txt and setup.py: 
https://caremad.io/posts/2013/07/setup-vs-requirement/

# OLD

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
