--  script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows FROM hbtn_0d_tvshows JOIN tv_shows_genres ON hbtn_0d_tvshows (id);
