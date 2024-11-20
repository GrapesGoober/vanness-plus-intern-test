-- Author: Nachat Kaewmeesang
-- This code is used for internship for Vanness Plus Consulting Co., Ltd
-- init.sql is used by the compose.yaml to initialize the container
-- This only runs once. Make sure to remove the volume if you need to reinitialize it.

CREATE DATABASE interns_db;
USE interns_db;
CREATE TABLE interns (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `applied_date` DATE NOT NULL,
    `role` VARCHAR(50) NOT NULL,
    `status` ENUM('New', 'WIP', 'Wait', 'Pass', 'Fail', 'Hire')
        NOT NULL DEFAULT 'New'
);