import pandas as pd

df = pd.read_csv("car details v4.csv")

print(df.columns.tolist())
print(df.head())