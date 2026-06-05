import glob
import os
import random

import face_recognition
import psycopg2

import p0


def connect_db():
    conn = psycopg2.connect(
        dbname="postgres", user="postgres", password="123", host="localhost"
    )
    return conn


LIMIT = 1000


if __name__ == "__main__":
    conn = connect_db()

    with conn.cursor() as cursor:
        cursor.execute("truncate face_embeddings")

    count = 0

    print("Leyendo directorio...")
    paths = list(glob.iglob(os.path.join(p0.DATASET_PATH, "**", "*.jpg")))

    print("Sacando sample...")
    path_sample = random.sample(paths, 1000)

    print("Insertando embeddings...")

    for path in path_sample:
        name = path.split("/")[-2]
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if not encodings:
            continue

        embedding = encodings[0].tolist()

        with conn.cursor() as cursor:
            cursor.execute(
                "insert into face_embeddings (name, path, embedding) values (%s, %s, %s)",
                (name, path, embedding),
            )

    conn.commit()
    conn.close()
