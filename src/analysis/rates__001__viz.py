import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from project_paths import RATES_FINAL


df = pd.read_parquet(RATES_FINAL)


sns.lineplot(data=df, x="date", y="EUR_DKK")
sns.lineplot(data=df, x="date", y="EUR_DKK__cross_USD")
sns.lineplot(data=df, x="date", y="EUR_DKK__cross_GBP")
sns.lineplot(data=df, x="date", y="EUR_DKK__cross_JPY")
plt.grid(axis="y")
plt.legend(["a", "b", "c", "d"])
plt.show()


ax = df.set_index("date")[["EUR_DKK", "EUR_DKK__cross_USD",
                           "EUR_DKK__cross_GBP", "EUR_DKK__cross_JPY"]].plot(fontsize=12)
ax.set_xlabel('Date')
ax.legend(fontsize=8)
plt.grid(axis="y")
plt.show()
