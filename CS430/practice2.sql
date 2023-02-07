CREATE OR REPLACE FUNCTION wow(one int, two int) RETURNS int AS $$
BEGIN 
RAISE NOTICE 'Price was raised; reverting'; 
IF (one < two) 
THEN 
Return two;
END IF; 

IF (two < one) 
THEN 
Return one;
END IF; 
 
RETURN NULL; 
END; 
$$ 
LANGUAGE plpgsql;
