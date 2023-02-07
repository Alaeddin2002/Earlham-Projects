SELECT C.stype
FROM Classes C
JOIN Ships S ON C.class = S.class
WHERE C.country = 'Gt. Britain';

SELECT C.stype
FROM Classes C
NATURAL JOIN ships
WHERE C.country = 'Gt. Britain';

SELECT C.displacement
FROM Classes C, ships S
WHERE C.class =s.class AND s.name = 'Musashi';

SELECT C.displacement
FROM Classes C
WHERE C.class = (SELECT S.class FROM ships S WHERE S.name = 'Musashi');

SELECT P.maker
FROM Product P, PC C
WHERE P.model = C.model AND hd>100;

SELECT C.price
FROM Product P, PC C
WHERE P.model = C.model AND P.maker = 'A';

SELECT maker
FROM Product
WHERE model IN (SELECT model FROM PC  WHERE  hd>100);

SELECT price
FROM PC
WHERE model IN (SELECT model FROM Product WHERE maker = 'A');