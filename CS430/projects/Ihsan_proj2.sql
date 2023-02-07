\d Netflix_Dataset_Movie;
--Movie_ID of type Integer is the unique value of every movie, which is also used as the key in the table
--Year_ of type Integer is the year that each movie was released..
-- Name of Char(500) is the name of each movie
\d Netflix_Dataset_Rating;
--User_ID of type integer is the value of the ID of the critique that rated the movie
--Rating of type integer is the rating of the movie from 1-5,
--Movie_ID of type Integer is the what movie was used in that row
--Key_ of type Integer is the unique value of every movie, which is also used as the key in the table

SELECT COUNT (Movie_ID) FROM Netflix_Dataset_Movie;
SELECT COUNT (User_ID) FROM Netflix_Dataset_Rating;