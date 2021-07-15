/*ДЕЛАЛ ВСЕ В SQLite
первое задание
это дает возможность выполнить первую часть задание вид с учетом данных лишь в географистатистикс*/
SELECT DIM_Geography.ParentID, DIM_Geography.Name, DIM_Geography.Type, FACT_GeographyStatistics.Date, FACT_GeographyStatistics.Population
FROM
	DIM_Geography
INNER JOIN FACT_GeographyStatistics ON FACT_GeographyStatistics.GeographyID=DIM_Geography.ID
ORDER BY Name
/* второе задание
это фактически тоже самое только я использую другой джоин*/
SELECT DIM_Geography.ParentID, DIM_Geography.Name, DIM_Geography.Type, FACT_GeographyStatistics.Date, FACT_GeographyStatistics.Population
FROM
	DIM_Geography
LEFT JOIN FACT_GeographyStatistics ON FACT_GeographyStatistics.GeographyID=DIM_Geography.ID
ORDER BY Name

/*Третье задание
bunch of left join together with each other and at the end the where clause to sort the result asked stackto help https://stackoverflow.com/posts/68365075/edit*/
SELECT
	coalesce (g5.Name, g4.Name, g3.Name, g2.Name, g1.Name) AS 'Name1', coalesce (g5.Type, g4.Type, g3.Type, g2.Type, g1.Type) AS 'Type1',
	coalesce (g4.Name, g3.Name, g2.Name, g1.Name, g2.Name, g3.Name, g4.Name, g5.Name) AS 'Name2', coalesce (g4.Type, g3.Type, g2.Type, g1.Type, g2.Type, g3.Type, g4.Type, g5.Type) AS 'Type2',
	coalesce (g3.Name, g2.Name, g1.Name, g2.Name, g3.Name, g4.Name) AS 'Name3', coalesce (g3.Type, g2.Type, g1.Type, g2.Type, g3.Type, g4.Type) AS 'Type3',
	coalesce (g2.Name, g1.Name, g2.Name, g3.Name) AS 'Name4', coalesce (g2.Type, g1.Type, g2.Type, g3.Type) AS 'Type4',
	coalesce (g1.Name, g2.Name, g3.Name) AS 'Name5', coalesce (g1.Type, g2.Type, g3.Type) AS 'Type5'
FROM DIM_Geography g5 LEFT JOIN
	DIM_Geography g4
	ON g4.ParentID = g5.ID LEFT JOIN
	DIM_Geography g3
	ON g3.ParentID = g4.ID LEFT JOIN
	DIM_Geography g2
	ON g2.ParentID = g3.ID LEFT JOIN
	DIM_Geography g1
	ON g1.ParentID = g2.ID
Where g5.Type = 'федеральный округ' AND Type5 = 'город'
/* задание 5, не получается его сделать. В теории, скорее всего у меня порблема с выводом во втором задании.
 Оно слишком громозкое и повторяющееся, из-за чего применить его для отсеивания 
 по федеральному округу не получется. И конечно же у меня нету идеи как отсеить по годам размер популяции
 */
SELECT DIM_Geography.Name ||' '|| DIM_Geography.Type AS 'geo',
	strftime('%D%M%Y',FACT_GeographyStatistics.Date), sum(FACT_GeographyStatistics.Population)
FROM
	DIM_Geography
INNER JOIN FACT_GeographyStatistics ON FACT_GeographyStatistics.GeographyID=DIM_Geography.ID
WHERE g5.ID=FACT_GeographyStatistics.GeographyID