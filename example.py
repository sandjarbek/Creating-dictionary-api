import pandas as pd
df = pd.read_csv("dictionary.csv")

print(df["word"])

definition = df.loc[df["word"]=="acidity"]["definition"].squeeze()
print(definition)