--  lists all genres from hbtn_0d_tvshows 
SELECT tv_shows.title, tv_show_genres.genre_id
COUNT(tv_shows.id) AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_shows.id
ORDER BY number_of_shows DESC;
