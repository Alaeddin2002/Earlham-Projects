CREATE OR REPLACE FUNCTION preventPCPriceIncrease() RETURNS
trigger AS
$$
BEGIN
 IF (OLD.price < NEW.price)
 THEN
 RAISE NOTICE 'Preventing price increase';
 RETURN NULL;
 END IF;
 RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER PCPriceTrigger
AFTER UPDATE OF price ON PC
FOR EACH ROW
WHEN (OLD.price < NEW.price)
 EXECUTE PROCEDURE revertPCPrice();
UPDATE PC
SET price = '$1000'
WHERE model = 1003;