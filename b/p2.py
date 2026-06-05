import face_recognition

import p1

if __name__ == "__main__":
    conn = p1.connect_db()

    sample_path = "../sample.jpeg"

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

    print("====================================================================")
    print("Búsqueda con coseno")
    print("====================================================================")
    print()
    print(result)

    with conn.cursor() as cursor:
        cursor.execute(
            """
            explain analyze
            select
            id, name, embedding,
            (%s::vector <=> embedding) as distance
            from face_embeddings
            order by distance limit %s
            """,
            (embedding, k),
        )
        result = cursor.fetchall()

    print()
    print()
    print("====================================================================")
    print("Búsqueda con coseno (plan de ejecución)")
    print("====================================================================")
    print()
    print("\n".join([tup[0] for tup in result]))

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

    print()
    print()
    print("====================================================================")
    print("Búsqueda con distancia euclidiana")
    print("====================================================================")
    print()
    print(result)

    with conn.cursor() as cursor:
        cursor.execute(
            """
            explain analyze
            select
            id, name, embedding,
            (%s::vector <-> embedding) as distance
            from face_embeddings
            order by distance limit %s
            """,
            (embedding, k),
        )
        result = cursor.fetchall()

    print()
    print()
    print("====================================================================")
    print("Búsqueda con distancia euclidiana (plan de ejecución)")
    print("====================================================================")
    print()
    print("\n".join([tup[0] for tup in result]))

    conn.commit()
    conn.close()
