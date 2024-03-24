import pandas as pd
from project_paths import EUR_RATES_RAW, EUR_RATES_PROCESSED


# Load dataset
df = pd.read_csv(EUR_RATES_RAW)

# Drop columns
df = df.drop(columns=["TIME PERIOD"])

# Rename columns
df = df.rename(columns={
    "DATE": "date",
    "UK pound sterling/Euro (EXR.D.GBP.EUR.SP00.A)": "EUR_GBP",
    "Japanese yen/Euro (EXR.D.JPY.EUR.SP00.A)": "EUR_JPY",
    "US dollar/Euro (EXR.D.USD.EUR.SP00.A)": "EUR_USD"
})

# Date cols
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# Float cols
float_cols = ["EUR_GBP", "EUR_JPY", "EUR_USD"]
df[float_cols] = df[float_cols].astype(float)

# Ad-hoc missing values analysis
df.isna().sum(axis=0)
mask__some_rate_missing = 0 < df[float_cols].isna().sum(axis=1)
df.loc[mask__some_rate_missing, float_cols] = df[float_cols].interpolate().loc[mask__some_rate_missing]

# Validation check
df.isna().sum(axis=0)

# Export
df.to_parquet(EUR_RATES_PROCESSED)
