import os


# Directories
RAW_DATA = os.path.join("data", "raw")
PROCESSED_DATA = os.path.join("data", "processed")

# Files
DKK_RATES_RAW = os.path.join(RAW_DATA, "202432301053455703709DNVALD00929048219.csv")
EUR_RATES_RAW = os.path.join(RAW_DATA, "ECB Data Portal_20240323004431.csv")
DKK_RATES_PROCESSED = os.path.join(PROCESSED_DATA, "DKK_RATES")
EUR_RATES_PROCESSED = os.path.join(PROCESSED_DATA, "EUR_RATES")
