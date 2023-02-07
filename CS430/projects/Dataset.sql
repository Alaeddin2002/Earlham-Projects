drop table if exists Netflix_Dataset_Movie cascade; 
CREATE TABLE Netflix_Dataset_Movie (
Movie_ID int,
Year_ int,
Name varchar(500),
primary key(Movie_ID)
);

drop table if exists Netflix_Dataset_Rating; 
CREATE TABLE Netflix_Dataset_Rating (
User_ID int,
Rating int,
Movie_ID int,
key_ int,
primary key (key_) 
);

