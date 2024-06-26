# Summary
This is Juan Kania-Morales' repository which contains sample analyses:

1.  case:
    * [Python Exercise](src/analysis/Python_Exercise1.ipynb)
2.  case:
    * [SQL Exercise 1](src/analysis/SQL_Exercise1.ipynb)
    * [SQL Exercise 2](src/analysis/SQL_Exercise2.ipynb)
    * [SQL Exercise 3](src/analysis/SQL_Exercise3.ipynb)

--------------------------------------------------------------------------------
# Reproducibility (~5 minutes)
1. Clone this repository to your working environment
2. Create isolated python environment named .venv:\
```"<python path>" -m venv "<git repository path>\.venv"```\
Recommended version of python is 3.10.6 or higher.
3. Activate the environment and install requirements.txt: ```pip install -r requirements.txt```
4. Run tests with ```pytest -v --tb=no --no-header```
5. Run data setup script ```sh setup.sh```.
6. You are ready to run existing analyses from **src/analysis**
