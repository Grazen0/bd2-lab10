begin transaction;
create extension if not exists cube;

create table if not exists vectors (
  id serial primary key,
  vector_lineal cube,
  vector_gist cube
);

insert into vectors(vector_lineal)
select cube(ARRAY[
  round(random()*1000),
  round(random()*1000)
  ]) from generate_series(1, 1000);

update vectors set vector_gist = vector_lineal;

create index if not exists idx_vectors_gist on vectors using gist(vector_gist);

explain analyze
with q as (
  select '(636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616)'::cube as query
) select *, cube_distance(vector_lineal, q.query) as D
from vectors cross join q
order by vector_lineal <-> q.query
limit 5;

explain analyze
with q as (
  select '(636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616)'::cube as query
) select *, cube_distance(vector_gist, q.query) as D
from vectors cross join q
order by vector_gist <-> q.query
limit 5;

create table if not exists dry_beans_tmp (
  Area numeric,
  Perimeter numeric,
  MajorAxisLength numeric,
  MinorAxisLength numeric,
  AspectRation numeric,
  Eccentricity numeric,
  ConvexArea numeric,
  EquivDiameter numeric,
  Extent numeric,
  Solidity numeric,
  roundness numeric,
  Compactness numeric,
  ShapeFactor1 numeric,
  ShapeFactor2 numeric,
  ShapeFactor3 numeric,
  ShapeFactor4 numeric,
  Class varchar
);

\copy dry_beans_tmp from 'dry_beans.csv' delimiter ',' csv header;

create table if not exists dry_beans (
  id serial primary key,
  features_seq cube,
  features_idx cube
);

insert into dry_beans (features_seq) select cube(ARRAY[
  Area,
  Perimeter,
  MajorAxisLength,
  MinorAxisLength,
  AspectRation,
  Eccentricity,
  ConvexArea,
  EquivDiameter,
  Extent,
  Solidity,
  roundness,
  Compactness,
  ShapeFactor1,
  ShapeFactor2,
  ShapeFactor3,
  ShapeFactor4
  ]) from dry_beans_tmp;

update dry_beans set features_idx = features_seq;
create index if not exists idx_dy_beans_features_gist on dry_beans using gist (features_idx);

explain analyze
with q as (
  select '(636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616)'::cube as query
) select *, cube_distance(features_seq, q.query) as D
from dry_beans cross join q
order by features_seq <-> q.query
limit 32; -- 2 4 8 16 32

explain analyze
with q as (
  select '(636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616, 636, 616)'::cube as query
) select *, cube_distance(features_idx, q.query) as D
from dry_beans cross join q
order by features_idx <-> q.query
limit 32; -- 2 4 8 16 32
rollback;
