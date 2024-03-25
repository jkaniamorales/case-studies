import pandas as pd
from project_paths import DKK_RATES_PROCESSED, EUR_RATES_PROCESSED, RATES_FINAL


# Load
df1 = pd.read_parquet(DKK_RATES_PROCESSED)
df2 = pd.read_parquet(EUR_RATES_PROCESSED)

# Reorder columns
df2 = df2[["date", "EUR_USD", "EUR_GBP", "EUR_JPY"]]

# Merge
df = df1.merge(df2, how="left")

# New columns
df["EUR_DKK__cross_USD"] = df["EUR_USD"] * df["USD_DKK"]
df["EUR_DKK__cross_GBP"] = df["EUR_GBP"] * df["GBP_DKK"]
df["EUR_DKK__cross_JPY"] = df["EUR_JPY"] * df["JPY_DKK"]

# Reorder columns
priority_cols = ["date", "EUR_DKK", "EUR_DKK__cross_USD", "EUR_DKK__cross_GBP", "EUR_DKK__cross_JPY"]
df = df[[x for x in priority_cols] + [x for x in df.columns if x not in priority_cols]]

# Extract
df.to_parquet(RATES_FINAL)
