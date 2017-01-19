drop table if exists entries;
create table entries (
  page text not null,
  field text not null,
  'text' text,
  image_id integer foreign key default null,
  -- compound primary key for page and title
  primary key (page, field)
);

drop table if exists images;
create table images (
  id integer primary key autoincrement,
  entry_id integer foreign key not null,
  path text not null
);

drop table if exists files;
create table files (
  id integer primary key autoincrement,
  page text not null,
  field text not null,
  path text not null
);

drop table if exists flags;
create table flags (
  id integer primary key autoincrement,
  page text not null,
  field text not null,
  flag integer default null
);

-- -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

insert into entries (page, field, text) values ("home", "title", "example title text");
insert into entries (page, field, text) values ("home", "description", "example description text");

insert into entries (page, field, text) values ("about", "title", "About Us");





