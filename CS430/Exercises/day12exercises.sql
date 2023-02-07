--a
INSERT INTO product values ('E','1200','laptop') ; INSERT INTO laptop values('1200','2.5','1024','100','19.7','2100');
SELECT * FROM product NATURAL JOIN laptop;

\i 2-4-1-creates.sql
\i 2-4-1-inserts.sql
--b
DELETE FROM PC
WHERE hd<100;
SELECT *
FROM pc

\i 2-4-1-creates.sql
\i 2-4-1-inserts.sql
--c
DELETE FROM printer WHERE MODEL IN (SELECT model FROM product WHERE type = 'printer' AND maker in (SELECT maker
FROM product EXCEPT (SELECT maker FROM product
WHERE type = 'laptop')));

DELETE FROM PRODUCT WHERE MODEL IN (SELECT model FROM product WHERE type = 'printer' AND maker in (SELECT maker
FROM product EXCEPT (SELECT maker FROM product
WHERE type = 'laptop')));

SELECT DISTINCT * FROM printer;                     
SELECT DISTINCT * FROM product;

\i 2-4-1-creates.sql
\i 2-4-1-inserts.sql
--d
UPDATE Product
SET maker = 'A'
WHERE maker = 'B';
SELECT * FROM product;                     

\i 2-4-1-creates.sql
\i 2-4-1-inserts.sql
--e
UPDATE PC
SET RAM =  RAM * 2, hd = hd + 60;
SELECT * FROM PC;
                     
\i 2-4-1-creates.sql
\i 2-4-1-inserts.sql
--f
UPDATE laptop
SET price = price - '$100', screen = screen + 1
WHERE model in (SELECT model FROM product WHERE maker = 'B');
SELECT * FROM laptop;
 
\i 2-4-1-creates.sql
\i 2-4-1-inserts.sql
                     
--e 
                     
INSERT INTO product(select maker,model+1100,'laptop' from product WHERE type = 'pc');                     
INSERT INTO
laptop(SELECT model+1100,speed,ram,hd,17,price-500::money from pc);
SELECT * FROM laptop;
SELECT * FROM product;
                     
                     