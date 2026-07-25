-- DecodeLabs Project 3 - The Data Warehouse
-- Table: Interns (Name, Role, Email)

CREATE TABLE IF NOT EXISTS Interns (
  id SERIAL PRIMARY KEY,
  Name  VARCHAR(100) NOT NULL,
  Role  VARCHAR(100) NOT NULL,
  Email VARCHAR(150) NOT NULL UNIQUE
);
