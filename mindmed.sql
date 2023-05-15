CREATE DATABASE  Mindmed

DROP TABLE member;
drop TABLE employee;
DROP TABLE pomodoro;



DROP TABLE member;

CREATE TABLE member (
  memberID INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(255),
  date_of_birth VARCHAR(255),
  mobail_number VARCHAR(255),
  email VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  department VARCHAR(255),
  comment VARCHAR(255)
);



CREATE TABLE employee (
  employeeID INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(255),
  date_of_birth VARCHAR(255),
  mobail_number VARCHAR(255),
  email VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  department VARCHAR(255),
  comment VARCHAR(255)
);

DROP TABLE pomodoro;

CREATE TABLE pomodoro (
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  department VARCHAR(255),
  num_of_session VARCHAR(255),
  date_of_session date
);

