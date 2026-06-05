import pandas as pd

df_data = pd.read_excel("DryBeanDataset/Dry_Bean_Dataset.xlsx")
df_data.to_csv("dry_beans.csv", index=False)
