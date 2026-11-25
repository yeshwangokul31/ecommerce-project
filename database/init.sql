
CREATE DATABASE IF NOT EXISTS ecommerce;

USE ecommerce;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, price, description)
VALUES
('Laptop', 55000.00, 'High performance laptop'),
('Smartphone', 25000.00, 'Latest Android smartphone'),
('Headphones', 2500.00, 'Wireless headphones');
