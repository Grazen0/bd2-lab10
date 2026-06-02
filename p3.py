import pandas as pd
from scipy.io.arff import loadarff


def insert_beans(df):
    for tup in df.values:
        cube = f"'({tup[0]}, {tup[1]}, {tup[2]}, {tup[3]}, {tup[4]}, {tup[5]}, {tup[6]}, {tup[7]}, {tup[8]}, {tup[9]}, {tup[10]}, {tup[11]}, {tup[12]}, {tup[13]}, {tup[14]}, {tup[15]})'"
        query = f"insert into dry_beans (features_seq) values ({cube}::cube);"
        print(query)


raw_data = loadarff("DryBeanDataset/Dry_Bean_Dataset.arff")
df_data = pd.DataFrame(raw_data[0])

insert_beans(df_data)
