/*
the database for this mini project is called indian exams this will modxel the indan education and examination system
*/

-- first we are creating the database 
CREATE DATABASE IF NOT EXISTS indian_exams;
use indian_exams;

-- creating an entity called pu college that represents all the indian colleges that teach in 11th and 12th grade students
CREATE TABLE PU_college (
    college_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    type ENUM('Science', 'Commerce', 'Arts') NOT NULL,
    annual_fee DECIMAL(10, 2) NOT NULL,
    capacity INT NOT NULL,
    contact_email VARCHAR(255), 
    contact_phone VARCHAR(20),
    college_description TEXT
);

-- creating a table called university that takes in student for the under graduate program
CREATE TABLE UNIVERSITY (
    university_id INT NOT NULL,
    campus VARCHAR(255) NOT NULL,
    annual_fee DECIMAL(10, 2) NOT NULL,
    location VARCHAR(255) NOT NULL,
    capacity INT NOT NULL,
    NIRF_ranking INT,
    university_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (university_id, campus)
);

-- a saperate table is created for the branch attribute as it is multivalued because each university provides courses in multiple branches

CREATE TABLE University_Branches (
    branch_id INT PRIMARY KEY,
    university_id INT NOT NULL,
    campus VARCHAR(255) NOT NULL,
    branch_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (university_id, campus) REFERENCES UNIVERSITY(university_id, campus)
);

-- research publications is a weak entity that is identified by the university

CREATE TABLE Research_Publications (
    university_id INT NOT NULL,
    campus VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    paper_id INT NOT NULL,
    topic_of_research TEXT,
    reference TEXT,
    PRIMARY KEY (university_id, campus, Author, paper_id),
    FOREIGN KEY (university_id, campus) REFERENCES UNIVERSITY(university_id, campus)
);

-- ceating an attribute called tutions that represents th extra classes that the students take to clear the various entrance exams
CREATE TABLE Tutions (
    tution_name VARCHAR(255) PRIMARY KEY,
    target_exams VARCHAR(255),
    mode ENUM('online', 'offline') NOT NULL,
    courses VARCHAR(255)
);

-- creating the student atttribute 
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    mail_id VARCHAR(255),
    phone_number VARCHAR(20),
    date_of_birth DATE,
    school VARCHAR(255),
    gender ENUM('Male', 'Female', 'Other'),
    address VARCHAR(255)
);

-- relation enrolls to represent the enrollment of a student into tutions
-- Create a junction table to represent the many-to-many relationship
CREATE TABLE Tution_enrollment (
    student_id INT NOT NULL,
    tution_name VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    timings VARCHAR(255),
    duration VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (tution_name) REFERENCES Tutions(tution_name),
    PRIMARY KEY (student_id, tution_name)
);


-- PU admission relation
CREATE TABLE PU_admission (
    admission_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    college_id INT NOT NULL,
    admission_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (college_id) REFERENCES PU_college(college_id)
);


CREATE TABLE University_admission (
    admission_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    university_id INT NOT NULL,
    admission_date DATE,
    scholarship DECIMAL(10, 2),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (university_id) REFERENCES UNIVERSITY(university_id)
);


-- creating an entity called exams to represent the exams taken by the students
CREATE TABLE Exam (
    exam_id INT AUTO_INCREMENT,
    Institute_name VARCHAR(225) NOT NULL,
    exam_name VARCHAR(255) NOT NULL,
    min_age INT NOT NULL,
    cut_off_marks DECIMAL(10, 2) NOT NULL,
    exam_date DATE NOT NULL,
    exam_duration INT,
    exam_type ENUM('Objective', 'Subjective', 'Combined'),
    max_attempts INT,
    college_id INT,
    university_id INT,
    PRIMARY KEY(exam_id),
    FOREIGN KEY (college_id) REFERENCES PU_college(college_id),
    FOREIGN KEY (university_id) REFERENCES university(university_id)
);

-- creating a results relation to represent a single student getting results in multiple exams
CREATE TABLE Result (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    exam_id INT NOT NULL,
    exam_name VARCHAR(255),
    date_of_result DATE,
    status ENUM('PASS', 'FAIL') NOT NULL,
    percent_marks DECIMAL(5, 2),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (exam_id) REFERENCES Exam(exam_id)
);



