import pandas as pd
from project_paths import DKK_RATES_PROCESSED, EUR_RATES_PROCESSED


# Load
df1 = pd.read_parquet(DKK_RATES_PROCESSED)
df2 = pd.read_parquet(EUR_RATES_PROCESSED)

# Merge
df = df1.merge(df2, how="left")

# Extract
df
