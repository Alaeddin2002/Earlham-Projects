--1
CREATE TRIGGER Age_100
AFTER INSERT ON household
FOR EACH ROW
WHEN (NEW.age_ > 100)
 EXECUTE PROCEDURE age();
 


CREATE OR REPLACE FUNCTION age() RETURNS trigger AS
$$
BEGIN
 IF ( NEW.age_ > 100)
 THEN
  RAISE NOTICE 'Wow age more than a hundred!?';
  RETURN NULL;
 END IF;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;

insert into household values ('Tex','04/02/2005',10, 2251, 'cat');
insert into household values ('Tex','04/02/2005',101, 3251, 'cat'); 

DROP TRIGGER Age_100 ON household;
 --2

CREATE TRIGGER price_NULL
BEFORE DELETE ON vet
FOR EACH ROW
WHEN (OLD.cost is NULL)
 EXECUTE PROCEDURE vetprice();
 
CREATE OR REPLACE FUNCTION vetprice() RETURNS trigger AS
$$
BEGIN
 IF (OLD.cost is NULL)
 THEN
     RAISE NOTICE 'can not delete when price is NULL';
     RETURN NULL;
 END IF;
 RETURN NEW; 
END;
$$
LANGUAGE plpgsql;

insert into vet values ('Rex',2001,'01/03/2006','vaccine');
DELETE FROM vet WHERE ID = 2001;

insert into vet values ('Rex',3001,'01/03/2006','vaccine',200);
DELETE FROM vet WHERE ID = 3001;

DROP TRIGGER price_NULL ON vet;

--3a
CREATE TRIGGER SumCost
BEFORE INSERT ON vet
FOR EACH ROW
 EXECUTE PROCEDURE totalcost();
 
 CREATE OR REPLACE FUNCTION totalcost() RETURNS trigger AS
$$
declare totalcost money;
BEGIN
 SELECT SUM(cost) into totalcost from vet;
 RAISE NOTICE 'The sum of costs is:%', totalcost;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;    

insert into vet values ('Rex',3001,'01/03/600','vaccine',200);
insert into vet values ('Rex',4001,'01/03/600','vaccine',200); --visit becomes existance

DROP TRIGGER SumCost ON vet;

--3b
CREATE TRIGGER SumCost
AFTER INSERT ON vet
FOR EACH ROW
 EXECUTE PROCEDURE totalcost();

CREATE OR REPLACE FUNCTION totalcost() RETURNS trigger AS
$$
declare totalcost money;
BEGIN
 SELECT SUM(cost) into totalcost from vet;
 RAISE NOTICE 'The sum of costs is:%', totalcost;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;  

insert into vet values ('Rex',3001,'01/03/600','vaccine',200);
insert into vet values ('Rex',4001,'01/03/600','vaccine',200); --visit becomes existance
--4

CREATE TRIGGER existing_name
BEFORE INSERT ON household
FOR EACH ROW
 EXECUTE Procedure name_exist();
 
 
CREATE OR REPLACE FUNCTION name_exist() RETURNS trigger AS
$$
BEGIN
 IF (NEW.name in (SELECT name FROM household))
  THEN 
     NEW.name = CONCAT(NEW.name,' jr');
     RETURN NEW;
 END IF;
 RETURN NEW;
END
$$
LANGUAGE plpgsql;     

insert into household values ('Tex','04/02/2005',10, 0251, 'cat');
insert into household values ('Demi','04/02/2005',10, 9251, 'cat');

DROP TRIGGER existing_name ON household;
                  