CREATE DATABASE transportation;
USE transportation;
-- customers table
CREATE TABLE  customers (
    customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    next_of_kin TEXT,
    next_of_kin_phone TEXT
);

-- trips table
CREATE TABLE  trips (
    trip_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    driver_id INT,
    bus_id INT,
    location VARCHAR(100) NOT NULL,
    trip_date DATETIME DEFAULT CURRENT_TIMESTAMP -- Date and time
    );

-- payments table (optional, if you want to track payments separately)
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    trip_id INTEGER,
    amount_paid REAL NOT NULL,
    payment_date DATE DEFAULT (CURRENT_DATE),
    payment_method ENUM('Cash', 'Card') NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id)
);