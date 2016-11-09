drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);

-- need to populate the entries with all the fields that need to be edited
