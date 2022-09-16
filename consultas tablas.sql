use esquema1;
select * from circuits;
-- DROP TABLE IF EXISTS drivers;
select * from drivers;-- revisar
select * from constructors;
select * from pit_stops;
select * from results;
select * from races;
select * from lap_times;
select * from qualifying;


#año con mayor cantidad de carreras
select * from races;
SELECT MAX(co.cant_carr) as 'cantidad maxima de carreras corridas en un anio' FROM 
   (SELECT count(year) as cant_carr 
    FROM races
    GROUP BY year) co;
    
SELECT year, count(year) as 'cantidad carreras corridas en el anio'
FROM races
GROUP BY year
ORDER BY count(year) DESC
LIMIT 5;
#Piloto con mayor cantidad de primeros puestos
select * from races;

SELECT MAX(gan.drivers) as 'cantidad carreras ganadas', gan.driverId as piloto FROM 
       (SELECT driverId, COUNT(driverId) as driver
       FROM results_filtrados
       WHERE positionOrder='1'
       GROUP BY driverId) gan;
       
#Nombre del circuito más corrido
SELECT count(r.circuitId), r.circuitId, r.name
FROM races r;


#Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
SELECT sum(r.points), r.driverId, d.surname
FROM results_filtrados r
JOIN drivers d
ON (r.driverId=d.driverId)
JOIN constructors_filtrados c
ON (c.constructorId=r.constructorId)
GROUP BY r.driverId and c.nationality="British" or c.nationality="American"
ORDER BY SUM(points) DESC;