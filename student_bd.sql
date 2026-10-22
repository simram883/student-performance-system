CREATE DATABASE student_management;

USE student_management;

CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(20),
    course VARCHAR(100),
    mobile VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255)
);