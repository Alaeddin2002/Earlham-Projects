SELECT maker, AVG(price::decimal)
FROM product,printer WHERE product.model = printer.model
GROUP BY maker;

SELECT maker,count(type)
FROM product
WHERE type = 'laptop'
GROUP BY maker
HAVING count(type) = 1;

SELECT maker,count(type)
FROM product NATURAL JOIN laptop
WHERE type = 'laptop' AND screen > 15
GROUP BY maker
HAVING count(type) = 1;

SELECT maker,count(type)
FROM product
GROUP BY maker
HAVING count(type) > 2 AND count(type) < 7;

SELECT maker,count(type)
FROM product WHERE type = 'pc'
GROUP BY maker
HAVING count(type) = (SELECT count(type) FROM product WHERE type = 'pc' AND maker = 'A' GROUP BY maker);

SELECT class, count(name)
FROM ships
GROUP BY class
HAVING count(name) = 1;

SELECT class, count(name)
FROM ships
GROUP BY class
Having count(name) >= ALL(SELECT count(name) FROM ships GROUP BY class) ;

SELECT class,count(NAME) 
FROM ships 
WHERE launched < '01/01/1930' 
GROUP BY class 
HAVING count(name) >= ALL (SELECT count(name)
FROM ships WHERE launched < '01/01/1930'
GROUP BY class);

SELECT maker, count(pc.model) 
FROM product NATURAL JOIN pc 
WHERE hd >= 250 
GROUP BY maker 
HAVING count(pc.model) >= ALL(SELECT count(pc.model)
FROM product NATURAL JOIN pc
WHERE hd>=250
GROUP BY maker);