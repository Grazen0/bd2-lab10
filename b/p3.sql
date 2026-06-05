alter table face_embeddings drop column if exists embedding_ivf_euc;
alter table face_embeddings drop column if exists embedding_ivf_cos;

alter table face_embeddings
    add column if not exists embedding_ivf_euc vector(128)
    generated always as (embedding) stored;

alter table face_embeddings
    add column if not exists embedding_ivf_cos vector(128)
    generated always as (embedding) stored;

create index if not exists face_embedding_index_ivf_euc
   on face_embeddings using ivfflat (embedding_ivf_euc) with (lists = 100);

create index if not exists face_embedding_index_ivf_cos
   on face_embeddings using ivfflat (embedding_ivf_cos vector_cosine_ops) with (lists = 100);

create index if not exists face_embedding_index_ivf
   on face_embeddings using ivfflat (embedding_ivf_cos vector_cosine_ops) with (lists = 100);
