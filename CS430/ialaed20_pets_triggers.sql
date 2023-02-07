--1
CREATE OR REPLACE FUNCTION age() RETURNS trigger AS
$$
BEGIN
 RAISE NOTICE 'Wow age more than a hundred!?';
 IF ( NEW.Birth > 100)
 THEN
 UPDATE household
 SET NEW.Birth = OLD.price
 WHERE ID = NEW.ID;
 END IF;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER Age_100
BEFORE Insert into birth ON household
FOR EACH ROW
WHEN (NEW.birth > 100)
EXECUTE PROCEDURE age();
 
 
 
CREATE OR REPLACE FUNCTION vetprice() RETURNS trigger AS
$$
BEGIN
 RAISE NOTICE 'Price was Null; reverting';
 IF ( NEW.price == "NULL")
 THEN
 UPDATE vet
 SET price = OLD.price
 WHERE model = NEW.model;
 END IF;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;