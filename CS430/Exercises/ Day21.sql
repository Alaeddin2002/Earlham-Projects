                                                                       
CREATE OR REPLACE FUNCTION price_with_conditional_tax_and_rent(price money, tax
real, cutoff money,rent money) RETURNS money AS
$$
declare
   first_name varchar(50) := 'John';
BEGIN
 IF (price > cutoff)
 THEN
 RETURN price * (1 + tax) - rent;
 END IF;
END;
$$
LANGUAGE plpgsql;
                                                                        

