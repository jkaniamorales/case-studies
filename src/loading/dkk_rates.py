import pandas as pd
from project_paths import DKK_RATES_RAW, DKK_RATES_PROCESSED


# Load dataset
df = pd.read_csv(DKK_RATES_RAW, skiprows=3)

# Rename columns
df = df.rename(columns={
    " ": "date",
    "Euro  (Jan. 1999-)": "EUR_DKK",
    "US Dollars  (Jan. 1977-)": "USD_DKK",
    "UK Pounds Sterling  (Jan. 1981-)": "GBP_DKK",
    "Japanese Yen  (Jan. 1981-)": "JPY_DKK"
})

# Missings values to None
df = df.replace("..", None)

# Date cols
df["date"] = pd.to_datetime(df["date"], format="%YM%mD%d")

# Float cols
float_cols = ["EUR_DKK", "USD_DKK", "GBP_DKK", "JPY_DKK"]
df[float_cols] = df[float_cols].astype(float)

# Normalize
# As-is state: rates are given as number of DKK per 100 units of foreign currency
# Target state: is that rates are given as number of DKK per 1 unit of foreign currency
df[float_cols] /= 100

# Number of missings
df.isna().sum(axis=0)

# Replace missings by linear interpolation
mask__some_rate_missing = 0 < df[float_cols].isna().sum(axis=1)
df.loc[mask__some_rate_missing, float_cols] = df[float_cols].interpolate().loc[mask__some_rate_missing]

# Validation check
df.isna().sum(axis=0)

# Export
df.to_parquet(DKK_RATES_PROCESSED)
