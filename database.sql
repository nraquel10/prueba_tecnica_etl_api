CREATE DATABASE prueba_tecnica;
USE prueba_tecnica;

CREATE TABLE companies (
    id VARCHAR(24) PRIMARY KEY,
    company_name VARCHAR(130)
);

CREATE TABLE charges (
    id VARCHAR(24) PRIMARY KEY,
    company_id VARCHAR(24),
    amount DECIMAL(16,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE OR REPLACE VIEW daily_transactions AS
SELECT
    company_id,
    DATE(created_at) AS transaction_day,
    SUM(amount) AS total_amount
FROM charges
GROUP BY company_id, DATE(created_at);
