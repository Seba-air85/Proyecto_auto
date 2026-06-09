import pandas as pd

df = pd.read_csv("dataset_final.csv")

print(df.shape)
print(df.columns.tolist())