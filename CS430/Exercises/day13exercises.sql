-- Notes:
--   reserved word conflicts, stype vs type, bdate vs date
--   data value conflict, 24 vs 24-27
-- 
-- You should add referential integrity (pk and fk at minimum) 

drop table if exists classes; 
create table classes(
class varchar(16), 
stype varchar(2), 
country varchar(16), 
numguns integer, 
bore integer, 
displacement integer,
primary key(class));


drop table if exists battles; 
create table battles(
  name varchar(16), 
  bdate date,
  primary key(name));
              
drop table if exists outcomes;
create table outcomes(
ship varchar(16), 
battle varchar(16), 
result varchar(16),
foreign key (battle) references battles(name) ON DELETE CASCADE, 
foreign key (ship) references ships(name) ON DELETE CASCADE); 
              
drop table if exists ships;
  create table ships(
  name varchar(16), 
  class varchar(16), 
  launched date,
primary key(name),
foreign key (name) references classes(class) ON DELETE CASCADE);






