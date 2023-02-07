SELECT model,speed
FROM laptop
WHERE speed >= All (SELECT speed FROM laptop);

SELECT P.maker
FROM Product P, PC C
WHERE C.model = P.model AND SPEED <= ALL (SELECT speed FROM PC);

SELECT C.model, P.model
FROM PC P, Printer C
WHERE P.price <= ALL (SELECT price FROM PC) AND C.price <= ALL(SELECT price FROM Printer);

SELECT C.model
FROM PC C
WHERE C.price <= ALL (SELECT price FROM Laptop);

SELECT model
FROM Laptop
WHERE price >= ALL (SELECT price FROM PC);

SELECT C.model
FROM PC P, Product C
WHERE C.maker = 'B' AND P.model = C.model AND P.price <= ALL (SELECT C.price FROM PC C, Product P WHERE P.maker='B' AND C.model = P.model);