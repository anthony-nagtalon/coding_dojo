-- Query 1: Countries that speak Slovene
SELECT countries.name, language, percentage
FROM languages
LEFT JOIN countries
ON languages.country_id = countries.id
WHERE languages.language = 'Slovene'
ORDER BY percentage DESC;

-- Query 2: Total Cities for each Country
SELECT countries.name, COUNT(cities.id) AS total_cities
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY total_cities DESC;

-- Query 3: All Cities in Mexico with > 500,000 pop.
SELECT cities.name, cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'Mexico'
ORDER BY cities.population DESC;

-- Query 4: All Languages in Each Country w/ > 89%
SELECT countries.name, language, percentage
FROM languages
LEFT JOIN countries
ON languages.country_id = countries.id
WHERE percentage > 0.89
ORDER BY percentage DESC;

-- Query 5: All Countries w/ Surface Area < 501 AND Pop. > 100,000
SELECT countries.name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

-- Query 6: Countries w/ Constitutional Monarchy AND Capital > 200 AND Life Exp. > 75 yrs.
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

-- Query 7: All Cities of Argentina inside Buenos Aires w/ Pop > 500,000
SELECT countries.name, cities.name, district, cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND district = 'Buenos Aires' AND cities.population > 500000;

-- Query 8: Number of Countries in each Region
SELECT region, COUNT(id) AS total_countries
FROM countries
GROUP BY region
ORDER BY total_countries DESC;