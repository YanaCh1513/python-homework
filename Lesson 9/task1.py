# %%
import pandas as pd

df = pd.read_csv("advertising_1.csv", index_col="Number")

df[:3]
df.head(3)

# %%
