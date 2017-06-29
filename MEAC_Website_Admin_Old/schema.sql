drop table if exists pages;
create table pages (
  id text primary key not null
--   many to one relationships to this table
);

drop table if exists entries;
create table entries (
  page text not null,
  field text not null,
  'text' text,
  -- compound primary key for page and title
  primary key (page, field)
);

drop table if exists images;
create table images (
  id integer primary key autoincrement,
  page text not null,
  field text not null,
  path text
);

drop table if exists files;
create table files (
  id integer primary key autoincrement,
  page text not null,
  field text not null,
  path text
);

drop table if exists flags;
create table flags (
  id integer primary key autoincrement,
  page text not null,
  field text not null,
  flag integer default 0
);

-- -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
insert into pages (id) values ("home");
insert into pages (id) values ("about");
insert into pages (id) values ("volunteer");

insert into entries (page, field, text) values ("home", "title", "example title text");
insert into entries (page, field, text) values ("home", "description", "example description text");
insert into entries (page, field, text) values ("about", "title", "About Us");
-- password for volunteer page
insert into entries (page, field, text) values ("volunteer", "password", "meac");

insert into images (page, field, path) values ("home", "logo", "../static/images/meac_logo_vector.svg");

insert into files (page, field, path) values ("home", "logo", "../static/images/meac_logo_vector.svg");

insert into flags (page, field, flag) values ("home", "emergency_notification", 1);

