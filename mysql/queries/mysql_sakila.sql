-- Query 1: Customers inside City ID 312
SELECT city.city_id, city, first_name, last_name, email, CONCAT(address, ' ', address2) AS address
FROM city
LEFT JOIN address
ON city.city_id = address.city_id
LEFT JOIN customer
ON address.address_id = customer.address_id
WHERE city.city_id = 312;

-- Query 2: All Comedy Films
SELECT film.film_id, title, description, release_year, rating, special_features, category.name
FROM category
LEFT JOIN film_category
ON category.category_id = film_category.category_id
LEFT JOIN film
ON film.film_id = film_category.film_id
WHERE category.name = 'Comedy';

-- Query 3: All Films joined by Actor ID 5
SELECT actor.actor_id, CONCAT(first_name, ' ', last_name) AS actor_name, film.film_id, film.title, description, release_year
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film.film_id = film_actor.film_id
WHERE actor.actor_id = 5;

-- Query 4: All Customers in Store ID 1 AND Inside Cities (1, 42, 312, 459)
SELECT store_id, city_id, first_name, last_name, email, CONCAT(address.address, ' ', address2) AS address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
WHERE store_id = 1 AND (city_id = 1 OR city_id = 42 OR city_id = 312 OR city_id = 459);

-- Query 5: All Films Rated G w/ Behind the Scenes, joined by Actor ID 15
SELECT title, description, release_year, rating, special_features
FROM film_actor
LEFT JOIN film
ON film.film_id = film_actor.film_id
WHERE actor_id = 15 AND rating = 'G' AND special_features LIKE '%Behind the Scenes%';

-- Query 6: All Actors in Film ID 369
SELECT film.film_id, title, actor.actor_id, CONCAT(first_name, ' ', last_name) AS actor_name
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

-- Query 7: All Drama Films with Rental Rate 2.99
SELECT film.film_id, title, description, release_year, rating, special_features, category.name AS genre
FROM category
LEFT JOIN film_category
ON category.category_id = film_category.category_id
LEFT JOIN film
ON film.film_id = film_category.film_id
WHERE rental_rate = 2.99 AND category.name = 'Drama';

-- Query 8: All Action Films joined by Sandra Kilmer
SELECT actor.actor_id, CONCAT(first_name, ' ', last_name) as actor_name, film.film_id, title, description, release_year, rating, special_features, category.name AS genre
FROM category
LEFT JOIN film_category
ON category.category_id = film_category.category_id
LEFT JOIN film
ON film.film_id = film_category.film_id
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND CONCAT(first_name, ' ', last_name) = 'SANDRA KILMER'