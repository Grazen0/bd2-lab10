import pandas as pd
from scipy.io.arff import loadarff

raw_data = loadarff("DryBeanDataset/Dry_Bean_Dataset.arff")
df_data = pd.DataFrame(raw_data[0])

df_data.to_csv("dry_beans.csv", index=False)
