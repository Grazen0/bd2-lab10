import heapq
import math

import pandas as pd

df = pd.read_excel("DryBeanDataset/Dry_Bean_Dataset.xlsx")

data = df.drop(columns=["Class"])
target = df["Class"]

# Normalizar usando min-max normalization
data = (data - data.min()) / (data.max() - data.min())


def dist(a, b):
    sum = 0

    for i in range(0, len(a)):
        sum += (a.iloc[i] - b.iloc[i]) ** 2

    return math.sqrt(sum)


def knn_search(idx: int, k: int):
    target = data.iloc[idx]
    max_heap = []

    for i in range(len(data)):
        if i == idx:
            continue

        row = data.iloc[i]
        heapq.heappush_max(max_heap, (dist(target, row), i))

        if len(max_heap) > k:
            heapq.heappop_max(max_heap)

    return [tup[1] for tup in max_heap]


query_idxs = [15, 2166, 4768]
ks = [2, 4, 8, 16, 32]

for q in query_idxs:
    q_class = target.iloc[q]

    for k in ks:
        results = knn_search(q, k)
        n = len(results)

        pr = 0
        for idx in results:
            if target.iloc[idx] == q_class:
                pr += 1

        pr /= n
        print(f"Q[{q}], k = {k}  =>  pr = {pr}, n = {n}")
