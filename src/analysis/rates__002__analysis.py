import pandas as pd
from project_paths import RATES_FINAL


df = pd.read_parquet(RATES_FINAL)

# EUR_DKK min
mask__EUR_DKK__min = df["EUR_DKK"] == df["EUR_DKK"].min()
df[mask__EUR_DKK__min]

# EUR_DKK max
mask__EUR_DKK__max = df["EUR_DKK"] == df["EUR_DKK"].max()
df[mask__EUR_DKK__max]
