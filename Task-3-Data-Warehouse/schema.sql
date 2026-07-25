-- DecodeLabs Project 3 - The Data Warehouse (Azure PostgreSQL)
-- Interns table with PRIMARY KEY, UNIQUE, NOT NULL

CREATE TABLE IF NOT EXISTS Interns (
  id SERIAL PRIMARY KEY,
  Name  VARCHAR(100) NOT NULL,
  Role  VARCHAR(100) NOT NULL,
  Email VARCHAR(150) NOT NULL UNIQUE
);
