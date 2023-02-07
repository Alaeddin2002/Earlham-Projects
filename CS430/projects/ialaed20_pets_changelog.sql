CREATE OR REPLACE FUNCTION ChangeLog() RETURNS
trigger AS
$$
BEGIN
 IF TG_OP = 'INSERT'
 THEN
 RAISE Notice 'Checking for INSERT into household';
 INSERT INTO changelog (pre, types) VALUES (NEW, TG_OP);
 RETURN NEW;
 ELSIF TG_OP = 'UPDATE'
 THEN
 RAISE Notice 'Checking for DELETE into household';
 INSERT INTO changelog (pre, types) VALUES (OLD, TG_OP);
 RETURN NEW;
 ELSIF   TG_OP = 'DELETE'
 THEN
 RAISE Notice 'Checking for DELETE ON household';
 INSERT INTO changelog (pre, types) VALUES (OLD, TG_OP);
 RETURN NEW;
 END IF;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER ChangeLog
AFTER INSERT OR UPDATE OR DELETE ON household
FOR EACH ROW
 EXECUTE PROCEDURE ChangeLog();
  
                                        