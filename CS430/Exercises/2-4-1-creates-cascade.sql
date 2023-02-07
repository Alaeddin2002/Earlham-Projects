drop table if exists pc;
CREATE TABLE pc (
model int,
speed decimal(3,2),
ram int,
hd int,
price money, 
foreign key (model) references product(model)
);

drop table if exists laptop; 
CREATE TABLE laptop (
model int,
speed decimal(3,2),
ram int,
hd int,
screen float,
price money,
foreign key (model) references product(model)
);

drop table if exists printer; 
CREATE TABLE printer (
model int,
color boolean,
type varchar(12),
price money,
foreign key (model) references product(model)
);
