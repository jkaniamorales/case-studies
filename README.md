# Introduction
This is Juan Kania-Morales' repository which contains sample analyses:
1. case 1:
    * [title1](src/analysis)
2. case 2:
    * [title2](src/analysis/SQL_Exercise1.ipynb)
    * [title3](src/analysis/SQL_Exercise2.ipynb)
    * [title4](src/analysis/SQL_Exercise3.ipynb)

--------------------------------------------------------------------------------
# Reproducibility (~5 minutes)
1. Clone this repository to your working environment
2. Create isolated python environment named .venv: ```"<python path>" -m venv "<git repository path>\.venv"```\
Recommended version of python is 3.10.6 or higher.
3. Activate the environment
4. Install requirements.txt: ```pip install -r requirements.txt```
5. Run tests with ```pytest -v --tb=no --no-header```
6. Run data setup script ```sh setup.sh```.
7. You are ready to run existing analyses from **src/analysis**
