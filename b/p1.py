import glob
import os

import face_recognition
import psycopg2

import p0


def connect_db():
    conn = psycopg2.connect()
    return conn


if __name__ == "__main__":
    conn = connect_db()

    with conn.cursor() as cursor:
        cursor.execute("truncate face_embeddings")

    count = 0

    for path in glob.iglob(os.path.join(p0.DATASET_PATH, "**", "*.jpg")):
        if count >= 1000:
            break

        count += 1

        name = path.split("/")[-2]

        image = face_recognition.load_image_file(path)

        encodings = face_recognition.face_encodings(image)
        if not encodings:
            print(f"Skipping {name}")
            continue

        embedding = encodings[0].tolist()

        with conn.cursor() as cursor:
            cursor.execute(
                "insert into face_embeddings (name, path, embedding) values (%s, %s, %s)",
                (name, path, embedding),
            )

    conn.commit()
    conn.close()
