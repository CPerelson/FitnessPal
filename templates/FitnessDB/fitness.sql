CREATE TABLE users(
    user_id INTEGER NOT NULL PRIMARY KEY, 
    user_name TEXT NOT NULL, 
    address_id INTEGER FOREIGN KEY,
    email TEXT, age INTEGER, 
    gender_id INTEGER FOREIGN KEY
);