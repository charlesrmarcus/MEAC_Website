drop table if exists entries;
create table entries (
  page text not null,
  field text not null,
  'text' text,
  -- compound primary key for page and title
  primary key (page, field)
);



insert into entries (page, field, text) values ("home", "title", "example title text");
insert into entries (page, field, text) values ("home", "description", "example description text");

insert into entries (page, field, text) values ("about", "title", "About Us");



