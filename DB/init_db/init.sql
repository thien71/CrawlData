CREATE DATABASE dienmaycholon;
USE dienmaycholon;

CREATE TABLE Product (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image VARCHAR(255),
    saleprice VARCHAR(20),
    discount VARCHAR(20)
);
