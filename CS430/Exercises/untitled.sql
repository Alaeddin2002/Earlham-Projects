DROP TRIGGER ProductModelTrigger ON PC;
CREATE TRIGGER ProductModelTrigger
BEFORE INSERT ON Product
FOR EACH ROW
WHEN (new.type = 'pc' AND(1000<NEW.model AND NEW.model <1999))
 EXECUTE PROCEDURE preventPCmodelchange();
 
CREATE OR REPLACE FUNCTION preventPCmodelchange() RETURNS
trigger AS
$$
BEGIN
 IF (new.type = 'pc' AND (1000<NEW.model AND NEW.model <1999))
 THEN
 RAISE NOTICE 'Preventing model change';
 RETURN NULL;
 END IF;
 RETURN OLD.model;
END;
$$
LANGUAGE plpgsql;

INSERT INTO Product ( maker,model,type)
VALUES ('A', 1888, 'pc');