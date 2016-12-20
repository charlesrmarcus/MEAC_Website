drop table if exists entries;
create table entries (
  -- id integer primary key autoincrement,
  page text not null,
  title text not null,
  'text' text not null,
  -- compound primary key for page and title
  primary key (page, title)
);

-- need to populate the entries with all the fields that need to be edited
insert into entries (title, page)
values ("index", "paragraph"), ("about", "employees");

