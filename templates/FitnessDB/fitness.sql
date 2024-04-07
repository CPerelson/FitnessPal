
/**
CREATE TABLE users(
    user_id INTEGER NOT NULL PRIMARY KEY, 
    user_name TEXT NOT NULL,
    email TEXT, 
    age INTEGER,
    address TEXT
);
**/
/**
ALTER TABLE users
ADD COLUMN gender_id INTEGER REFERENCES gender(gender_id);
**/
/**
CREATE TABLE statistics(
    statistics_id INTEGER NOT NULL PRIMARY KEY,
    weight INTEGER, 
    height INTEGER
);
forgein keys user_id, fitness_level_id
**/
/**
ALTER TABLE statistics
ADD COLUMN user_id INTEGER REFERENCES users(user_id);
**/
/**
ALTER TABLE statistics
ADD COLUMN fitness_level_id INTEGER REFERENCES fitness_level(fitness_level_id);
**/
/**
CREATE TABLE fitness_level(
    fitness_level_id INTEGER NOT NULL PRIMARY KEY,
    level_name TEXT
);
**/


CREATE TABLE gender(
    gender_id TEXT NOT NULL PRIMARY KEY,
    gender_name TEXT
);

/**PRAGMA foreign_keys = ON;**/

/**
NSERT INTO gender(gender_id, gender_name)
VALUES(f, 'female')
**/

/**DROP TABLE gender;**/

Select * from gender;