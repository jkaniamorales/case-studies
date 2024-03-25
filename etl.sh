echo "Activate environment..."
VENVPATH=".venv/Scripts/activate"
source $VENVPATH

echo "Run Raw Data Loaders"
python -m src.loading.dkk_rates
python -m src.loading.eur_rates
python -m src.loading.employees_db

echo "Run Processed Data Formation"
python -m src.formation.rates
