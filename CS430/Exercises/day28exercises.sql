CREATE TRIGGER LaptopSpeedTrigger
BEFORE UPDATE OF speed ON Laptop
FOR EACH ROW
WHEN (OLD.speed > NEW.speed)
 EXECUTE PROCEDURE LaptopSpeed();

CREATE OR REPLACE FUNCTION LaptopSpeed() RETURNS trigger AS
$$
BEGIN
 IF (OLD.speed > NEW.speed)
 THEN
     RAISE NOTICE 'Speed was Lowered; reverting';
     RETURN OLD;
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

--row trigger, will fire once for each row affected by the action.If we try to do an action on all of the tuples at once, it willfire N times, once for each tuple. If no rows are affected, the trigger does not fire.
--statement trigger,  will fire once for the entire action, no matter how many tuples are affected.


--After, the table data is affected after the execution of the action query where the action is still imploemented but a function acts after it, instead of disregarrd the action that triggers it and implements another action that is in a given function. 