
SELECT maker, price
FROM product, pc
WHERE pc.model = product.model AND speed >= 2.20;


SELECT pc.model,pc.price
FROM product,pc
WHERE maker = 'A' AND pc.model = product.model
UNION
SELECT laptop.model,laptop.price
FROM product,laptop
WHERE maker = 'A' AND laptop.model = product.model
UNION
SELECT printer.model,printer.price
FROM product,printer
WHERE maker = 'A' AND printer.model = product.model;


SELECT DISTINCT maker
from product
WHERE product.type = 'printer'
EXCEPT
SELECT DISTINCT maker
FROM product
WHERE product.type = 'laptop';


SELECT DISTINCT maker
from product
WHERE product.type = 'printer'
INTERSECT
SELECT DISTINCT maker
FROM product
WHERE product.type = 'pc';


SELECT DISTINCT Pc1.model
FROM pc Pc1, pc Pc2
WHERE Pc1.speed = Pc2.speed AND Pc1.model != Pc2.model;


SELECT model
FROM pc
EXCEPT
SELECT DISTINCT Pc1.model
FROM pc Pc1, pc Pc2
WHERE Pc1.speed = Pc2.speed AND Pc1.model != Pc2.model;


SELECT DISTINCT Pc1.model,Pc2.model,Pc1.hd
FROM pc Pc1, pc Pc2
WHERE Pc1.hd = Pc2.hd AND Pc1.model != Pc2.model AND Pc1.model < Pc2.model;

