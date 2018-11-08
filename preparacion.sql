DROP DATABASE IF EXISTS ormtest;
CREATE DATABASE ormtest;
CREATE USER 'guest'@'localhost' IDENTIFIED BY 'guest';
GRANT ALL ON ormtest.* TO 'guest'@'localhost';
