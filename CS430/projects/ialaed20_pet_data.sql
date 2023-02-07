drop table if exists household cascade; 
CREATE TABLE household (
name varchar(64),
birth date NOT NULL,
age_ int NOT NULL,
ID int NOT NULL,
type varchar(12) CHECK (type IN ('dog', 'cat', 'sheep', 'chicken', 'other')), 
primary key(ID)
);

drop table if exists vet cascade; 
CREATE TABLE vet (
name varchar(64) NOT NULL,
ID int NOT NULL,
visit date NOT NULL,
description varchar(64) NOT NULL, 
cost money,
foreign key (ID) references household (ID)
);

insert into household values ('Rex','07/02/2005',17, 1001, 'dog');
insert into household values ('Sally','06/04/2004',18, 1002, 'dog');
insert into household values ('Simba','01/03/2021',1, 2001, 'cat');
insert into household values ('Shawn','12/17/2014',8, 3001, 'sheep');
insert into household values ('feathers','10/13/2018',4, 4001, 'chicken');
      
insert into vet values ('Rex',2001,'01/03/2006','vaccine');
                        
insert into vet values ('Rex',1001,'01/03/2006','vaccine', 200);
insert into vet values ('Shawn',3001,'04/21/2017','checkup', 50);
insert into vet values ('Simba',2001,'01/03/2022','vaccine', 200);
insert into vet values ('Rex',1001,'09/13/2021','sick', 2000);   
insert into vet values ('feathers',4001,'08/13/2019','vaccine', 200);
insert into vet values ('feathers',4001,'07/03/2020','checkup', 100);
insert into vet values ('Shawn',3001,'01/01/2022','sick', 2000);
insert into vet values ('Shawn',3001,'04/21/2018','checkup', 50);
insert into vet values ('Sally',3001,'06/14/2014','checkup', 50);    

                        
SELECT name, AGE ('03,15,2022',birth) FROM household where name in (SELECT DISTINCT vet.name
FROM vet GROUP BY vet.name HAVING count(id) >= All( SELECT count(id) FROM vet GROUP BY name))
;                        
                                                   
SELECT name, count(id),sum(cost)
FROM vet
GROUP BY name;
                                                   
SELECT type,count(type)
FROM household
GROUP BY type;        
                                                  
SELECT name
FROM household
WHERE name in (select name FROM vet where cost < '$100');  
                                                   
SELECT type
FROM household
GROUP BY type
HAVING count(type) >= ALL(SELECT count(type) FROM household GROUP BY type);                                                   