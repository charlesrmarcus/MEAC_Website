drop table if exists entries;
create table entries (
  page text not null,
  title text not null,
  'text' text not null,
  -- compound primary key for page and title
  primary key (page, title)
);

-- need to populate the entries with all the fields that need to be edited
insert into entries (page, title)
values 
  -- home page
  ("home", "title"),

  -- about page
  ("about", "title"),

  -- contact page
  ("contact", "title"),

  -- events page
  ("events", "title"),

  -- gethelp page
  ("gethelp", "title"),

  -- getinvolved page
  ("getinvolved", "title"),

  -- history page
  ("history", "title"),

  -- meettheteam page
  ("meettheteam", "title"),

  -- supporters page
  ("supporters", "title"),

  -- whatshappening page
  ("whatshappening", "title")

;

