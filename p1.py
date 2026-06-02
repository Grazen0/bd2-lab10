import math

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("DryBeanDataset/Dry_Bean_Dataset.xlsx")

data = df.drop(columns=["Class"])
target = df["Class"]


# Normalizar usando min-max normalization
data = (data - data.min()) / (data.max() - data.min())


def dist(a, b):
    sum = 0

    for i in range(0, len(a)):
        sum += (a[i] - b[i]) ** 2

    return math.sqrt(sum)


def range_search(center_idx: int, radius: float) -> list[int]:
    center = data.loc[center_idx]
    result: list[int] = []

    for i in range(len(data)):
        if i == center_idx:
            continue

        row = data.iloc[i]

        if dist(row, center) <= radius:
            result.append(i)

    return result


dists = []

for _ in range(5000):
    a, b = data.sample(2).itertuples(index=False)
    dists.append(dist(a, b))

plt.hist(dists, bins=50)

plt.xlabel("Distancia")
plt.ylabel("Frecuencia")
plt.title("Distribución de distancias (5000 pares aleatorios)")

plt.show()

query_idxs = [15, 2166, 4768]
radiuses = [0.25, 0.3, 0.35, 0.4, 0.45]

for q in query_idxs:
    q_class = target.iloc[q]

    for r in radiuses:
        results = range_search(q, r)
        n = len(results)

        pr = 0
        for idx in results:
            if target.iloc[idx] == q_class:
                pr += 1

        pr /= n
        print(f"Q[{q}], r = {r}  =>  pr = {pr}, n = {n}")
