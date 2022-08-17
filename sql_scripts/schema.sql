CREATE DATABASE IF NOT EXISTS cazapp;
USE cazapp;

CREATE TABLE IF NOT EXISTS accounts (
    id int NOT NULL AUTO_INCREMENT,
    first_name varchar(50) NOT NULL,
    email varchar(100) NOT NULL UNIQUE,
    county varchar(100) NOT NULL,
    password varchar(255) NOT NULL,
    reg_number varchar(10) NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS support_requests (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(100) NOT NULL,
    message text NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (email) REFERENCES accounts (email)
);
