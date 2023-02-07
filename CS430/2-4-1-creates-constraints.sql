drop table if exists product cascade; 
CREATE TABLE product (
maker varchar(1),
model int,
type varchar(12)  CHECK (type IN ('pc', 'laptop', 'printer')), 
primary key(model)
);

drop table if exists pc;
CREATE TABLE pc (
model int,
speed decimal(3,2),
ram int,
hd int,
price money CHECK (price > 0), 
foreign key (model) references product(model)
);

drop table if exists laptop; 
CREATE TABLE laptop (
model int,
speed decimal(3,2),
ram int,
hd int,
screen float  CHECK (screen > 0),
price money CHECK (price > 0),
foreign key (model) references product(model)
);

drop table if exists printer; 
CREATE TABLE printer (
model int CHECK (model > 0),
color boolean,
type varchar(12),
price money CHECK (price > 0),
foreign key (model) references product(model)
);
