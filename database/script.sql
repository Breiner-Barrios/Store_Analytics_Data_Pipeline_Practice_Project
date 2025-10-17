-- Crear un nuevo esquema
CREATE SCHEMA IF NOT EXISTS store_analytics;
SET search_path TO store_analytics;
-- ========================
-- 1️⃣ Tabla de clientes
-- ========================
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    -- Se restringe el género a valores específicos para mantener la consistencia.
    gender VARCHAR(20) CHECK (gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    age INT CHECK (age > 0), -- La edad debe ser un valor positivo.
    city VARCHAR(100)
);

-- ========================
-- 2️⃣ Tabla de productos
-- ========================
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    -- El precio no puede ser negativo.
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    -- El stock no puede ser negativo.
    stock INT DEFAULT 0 CHECK (stock >= 0)
);

-- ========================
-- 3️⃣ Tabla de ventas
-- ========================
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id INT references customers(customer_id) ON DELETE CASCADE,
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
    sale_date DATE DEFAULT CURRENT_DATE,
    -- La cantidad vendida debe ser mayor que cero.
    quantity INT NOT NULL CHECK (quantity > 0)
    -- Se elimina la columna 'total'. Es mejor calcularla en las consultas (quantity * price)
    -- para evitar inconsistencias de datos.
);
