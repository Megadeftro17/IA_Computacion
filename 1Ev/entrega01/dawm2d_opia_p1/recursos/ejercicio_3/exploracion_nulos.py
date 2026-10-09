import pandas as pd
from sklearn.datasets import fetch_california_housing

df = fetch_california_housing(as_frame=True).frame
print("--- Valores nulos por columna ---")
print(df.isnull().sum())
df_clean = df.dropna()