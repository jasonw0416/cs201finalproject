CREATE DATABASE TrojanScheduler;
USE TrojanScheduler;

CREATE TABLE results(
	resultsID int(11) primary key not null auto_increment, 
    -- userID int(11) not null unique, 
    results JSON
    -- FOREIGN KEY fk2(userID) REFERENCES credentials(userID)
);

CREATE TABLE credentials (
	userID int(11) primary key not null auto_increment, 
    Username varchar(45) not null unique, 
    Password varchar(45) not null, 
    resultsID int(11), 
    FOREIGN KEY fk1(resultsID) REFERENCES results(resultsID)
);

CREATE TABLE professors (
	profID int(11) primary key not null auto_increment, 
    name varchar(45) not null unique, 
    rating double
);

CREATE TABLE courses (
	courseID int(11) primary key not null auto_increment, 
    CourseIDString varchar(255) not null,
    profID int(11) not null, 
    Course_Name varchar(2000) not null, 
    GE_Category varchar(2),
    monday TINYINT, 
    tuesday TINYINT, 
    wednesday TINYINT, 
    thursday TINYINT, 
    friday TINYINT, 
    StartTime int not null, 
    EndTime int not null,
    FOREIGN KEY fk2(profID) REFERENCES professors(profID)
);