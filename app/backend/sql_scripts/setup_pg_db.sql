--####################################################--
------------------ Creating Schemas --------------------
--####################################################--

CREATE SCHEMA IF NOT EXISTS test_schema;

--###############################################--
------------------ Test Database ------------------
--###############################################--

CREATE TABLE IF NOT EXISTS test_schema.test_table (
    column_name_1 INT NOT NULL,
    column_name_2 VARCHAR(200),
    column_name_3 FLOAT
	);

DELETE FROM test_schema.test_table;
INSERT INTO test_schema.test_table values (1, '1968', 2.1);
INSERT INTO test_schema.test_table values (2, '1969', 2.1);

--####################################################--
------------------ Ecommerce Database ------------------
--####################################################--

-- Users table
CREATE TABLE IF NOT EXISTS test_schema.users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    registration_date DATE NOT NULL,
    user_type TEXT CHECK (user_type IN ('admin', 'customer')) -- Assuming two types: admin and customer
);

-- Inserting data into test_schema.users
DELETE FROM test_schema.users;
INSERT INTO test_schema.users (username, password, email, registration_date, user_type) VALUES
('john_doe', 'password123', 'john.doe@example.com', '2023-10-19', 'customer'),
('alice_smith', 'securepass', 'alice.smith@example.com', '2023-09-15', 'admin');

---------------------------------------------------------------------------------------------------------

-- Supplier table
CREATE TABLE IF NOT EXISTS test_schema.supplier (
    supplier_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    contact_details VARCHAR
);

-- Inserting data into test_schema.supplier
DELETE FROM test_schema.supplier;
INSERT INTO test_schema.supplier (name, contact_details) VALUES
('TechSupplier Inc.', '1234 Tech St, Silicon Valley'),
('StyleHouse', '5678 Fashion Ave, New York');

---------------------------------------------------------------------------------------------------------

-- Product table
CREATE TABLE IF NOT EXISTS test_schema.product (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR,
    price FLOAT NOT NULL,
    stock_count INT NOT NULL,
    category VARCHAR,
    parent_product_id INT REFERENCES test_schema.product(product_id) -- Self-referencing for parent-child products
);

-- Adding a relationship between Product and Supplier
ALTER TABLE test_schema.product ADD COLUMN supplier_id INT REFERENCES test_schema.supplier(supplier_id);

-- Inserting data into test_schema.product
DELETE FROM test_schema.product;
INSERT INTO test_schema.product (name, description, price, stock_count, category, parent_product_id, supplier_id) VALUES
('Laptop', 'Dell XPS 13', 1000.50, 100, 'Electronics', NULL, 1),
('Fashion Hat', 'Stylish summer hat', 25.00, 200, 'Fashion', NULL, 2);

---------------------------------------------------------------------------------------------------------

-- Orders table
CREATE TABLE IF NOT EXISTS test_schema.orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES test_schema.users(user_id),
    order_date DATE NOT NULL,
    shipping_date DATE,
    status TEXT CHECK (status IN ('pending', 'shipped', 'delivered', 'cancelled')) -- Assuming some typical order statuses
);

-- Inserting data into test_schema.orders
DELETE FROM test_schema.orders;
INSERT INTO test_schema.orders (user_id, order_date, shipping_date, status) VALUES
(1, '2023-10-10', '2023-10-12', 'shipped'),
(2, '2023-09-20', '2023-09-23', 'delivered');

---------------------------------------------------------------------------------------------------------

-- OrderDetails table
CREATE TABLE IF NOT EXISTS test_schema.orderdetails (
    order_id INT REFERENCES test_schema.orders(order_id),
    product_id INT REFERENCES test_schema.product(product_id),
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id) -- Composite primary key
);

-- Inserting data into test_schema.orderdetails
DELETE FROM test_schema.orderdetails;
INSERT INTO test_schema.orderdetails (order_id, product_id, quantity) VALUES
(1, 1, 2),
(2, 2, 3);

---------------------------------------------------------------------------------------------------------

-- Payment table
CREATE TABLE IF NOT EXISTS test_schema.payment (
    payment_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES test_schema.orders(order_id),
    payment_method TEXT CHECK (payment_method IN ('credit_card', 'paypal', 'bank_transfer')), -- Assuming three payment methods
    payment_date DATE NOT NULL,
    amount FLOAT NOT NULL
);

-- Inserting data into test_schema.payment
DELETE FROM test_schema.payment;
INSERT INTO test_schema.payment (order_id, payment_method, payment_date, amount) VALUES
(1, 'credit_card', '2023-10-10', 2001.00),
(2, 'paypal', '2023-09-20', 75.00);

---------------------------------------------------------------------------------------------------------

-- Review table
CREATE TABLE IF NOT EXISTS test_schema.review (
    review_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES test_schema.product(product_id),
    user_id INT REFERENCES test_schema.users(user_id),
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Assuming a rating scale from 1 to 5
    review_text VARCHAR
);

-- Inserting data into test_schema.review
DELETE FROM test_schema.review;
INSERT INTO test_schema.review (product_id, user_id, rating, review_text) VALUES
(1, 1, 4, 'Good laptop but a bit expensive.'),
(2, 2, 5, 'Love this hat!');

---------------------------------------------------------------------------------------------------------

-- Wishlist table
CREATE TABLE IF NOT EXISTS test_schema.wishlist (
    wishlist_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES test_schema.users(user_id),
    product_id INT REFERENCES test_schema.product(product_id)
);

-- Inserting data into test_schema.wishlist
DELETE FROM test_schema.wishlist;
INSERT INTO test_schema.wishlist (user_id, product_id) VALUES
(1, 2);

---------------------------------------------------------------------------------------------------------

-- Shipment table
CREATE TABLE IF NOT EXISTS test_schema.shipment (
    shipment_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES test_schema.orders(order_id),
    tracking_number VARCHAR,
    carrier VARCHAR,
    estimated_arrival DATE
);

-- Inserting data into test_schema.shipment
DELETE FROM test_schema.shipment;
INSERT INTO test_schema.shipment (order_id, tracking_number, carrier, estimated_arrival) VALUES
(1, 'TRACK12345', 'FedEx', '2023-10-15'),
(2, 'TRACK67890', 'UPS', '2023-09-25');

---------------------------------------------------------------------------------------------------------