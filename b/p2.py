import face_recognition
import p1

if __name__ == "__main__":
    conn = p1.connect_db()

    sample_path = "sample.jpeg"

    image = face_recognition.load_image_file(sample_path)
    encodings = face_recognition.face_encodings(image)

    embedding = encodings[0].tolist()

    result = None
    k = 10
    with conn.cursor() as cursor:
        cursor.execute(
            """
            select
            id, name, embedding,
            (%s::vector <=> embedding) as distance
            from face_embeddings
            order by distance limit %s
            """,
            (embedding, k),
        )
        result = cursor.fetchall()

    print(result)

    with conn.cursor() as cursor:
        cursor.execute(
            """
            select
            id, name, embedding,
            (%s::vector <=> embedding) as distance
            from face_embeddings
            order by distance limit %s
            """,
            (embedding, k),
        )
        result = cursor.fetchall()

    print(result)

    with conn.cursor() as cursor:
        cursor.execute(
            """
            select
            id, name, embedding,
            (%s::vector <-> embedding) as distance
            from face_embeddings
            order by distance limit %s
            """,
            (embedding, k),
        )
        result = cursor.fetchall()

    print(result)

    with conn.cursor() as cursor:
        cursor.execute(
            """
            select
            id, name, embedding,
            (%s::vector <-> embedding) as distance
            from face_embeddings
            order by distance limit %s
            """,
            (embedding, k),
        )
        result = cursor.fetchall()

    print(result)

    conn.commit()
    conn.close()
