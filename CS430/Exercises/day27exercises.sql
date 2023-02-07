CREATE VIEW TRIAL AS SELECT * FROM Product NATURAL JOIN PC WHERE maker = 'A';
SELECT * FROM TRIAL WHERE hd > 200;


CREATE TRIGGER LaptopSpeedTrigger
AFTER UPDATE OF speed ON Laptop
FOR EACH ROW
WHEN (OLD.speed > NEW.speed)
 EXECUTE PROCEDURE LaptopSpeed();

CREATE OR REPLACE FUNCTION LaptopSpeed() RETURNS trigger AS
$$
BEGIN
 RAISE NOTICE 'Speed was Lowered; reverting';
 IF (OLD.speed > NEW.speed)
 THEN
 UPDATE Laptop
 SET speed = OLD.speed
 WHERE model = NEW.model;
 END IF;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;

update Laptop
set speed = '0.2' where model = '2007';

update Laptop
set speed = speed +'2' where model = '2007';

update Laptop
set screen = screen -'0.2' where model = '2007';