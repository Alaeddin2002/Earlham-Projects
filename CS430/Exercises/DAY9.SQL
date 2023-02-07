SELECT model,speed FROM laptop EXCEPT (SELECT DISTINCT c.model, c.speed
FROM Laptop c, Laptop a
WHERE c.speed < a.speed);

SELECT DISTINCT model, speed
FROM Laptop
ORDER BY speed DESC
LIMIT 1;


SELECT maker FROM Product WHERE model IN (SELECT model FROM PC EXCEPT (SELECT DISTINCT c.model
FROM PC c, PC a
WHERE c.speed > a.speed));
                                                                       
SELECT maker FROM Product WHERE model IN (SELECT model
FROM PC
ORDER BY speed
LIMIT 1);                                 
                                                                       
SELECT DISTINCT c.model, p.model FROM PC c, Printer p WHERE c.model IN (SELECT Model FROM PC EXCEPT (SELECT DISTINCT c.model
FROM PC c, PC d
WHERE c.price>d.price)) AND p.model IN(SELECT model FROM Printer EXCEPT (SELECT DISTINCT p.model FROM Printer p, Printer a WHERE p.price>a.price));
                                                                         
SELECT p.model,c.model FROM PC p, Printer c WHERE p.model IN (SELECT model
FROM PC
ORDER BY price
LIMIT 1) AND c.model IN (SELECT model FROM printer  ORDER BY price LIMIT 1)  ;  