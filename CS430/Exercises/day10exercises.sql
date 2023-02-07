SELECT name
FROM ships
WHERE launched in (SELECT max(launched) FROM ships)
LIMIT 1;

SELECT name
FROM ships
WHERE launched in(SELECT MAX(launched) FROM ships);

SELECT count(*)
FROM ships;

SELECT AVG(price::numeric)
FROM printer;

SELECt SUM(price)
FROM printer;

SELECT count(distinct(battles))
FROM battles;
                      
SELECT count(name)
FROM ships
WHERE class = 'Iowa';
                      
SELECt class, count(*)
FROM ships
GROUP BY class;
                      
SELECt class, count(*)
FROM ships
WHERE class in(SELECT class FROM Classes WHERE country = 'Gt. Britain')
GROUP BY class;                      