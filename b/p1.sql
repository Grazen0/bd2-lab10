create extension if not exists vector;

create table if not exists face_embeddings (
    id serial primary key,
    name text,
    path text,
    embedding vector(128)
);
