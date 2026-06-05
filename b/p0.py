import glob
import os

import matplotlib.pyplot as plt
import pandas as pd

DATASET_PATH = "lfwpeople/lfw_funneled"


def mostrarFotos(coleccion: pd.DataFrame, posiciones: list[int]):
    plt.figure(figsize=(16, 10))
    i = 0

    for idx in posiciones:
        img = plt.imread(coleccion.path.iloc[idx])
        plt.subplot(4, 4, i + 1)
        plt.imshow(img)
        plt.title(coleccion.person.iloc[idx] + str(img.shape))
        plt.xticks([])
        plt.yticks([])
        i += 1

    plt.tight_layout()
    plt.show()


def main():

    coleccion = []

    # modificado para linux
    for path in glob.iglob(os.path.join(DATASET_PATH, "**", "*.jpg")):
        person = path.split("/")[-2]
        coleccion.append({"person": person, "path": path})

    coleccion = pd.DataFrame(coleccion)

    posiciones = list(range(0, 16))
    mostrarFotos(coleccion, posiciones)


if __name__ == "__main__":
    main()
