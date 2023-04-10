-- List all shows contained in the db without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
RIGHT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
BY ORDER tv_shows.title ASC, tv_show_genres.genre_id ASC;
