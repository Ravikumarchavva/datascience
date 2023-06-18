-- Get a list of tables and views in the current database
SELECT table_catalog [database], table_schema [schema], table_name name, table_type type
FROM INFORMATION_SCHEMA.TABLES
GO


CREATE TABLE portfolio.Contact
(
    sl.no INT  PRIMARY KEY Autoincrement, -- primary key column
    name [NVARCHAR](50) NOT NULL,
    mail [NVARCHAR](50) NOT NULL,
    subject [NVARCHAR](50) NOT NULL,
    message [NVARCHAR](500) NOT NULL
    
    -- specify more columns here
);
GO

-- Create a new database called 'DatabaseName'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'Portfolio'
)
CREATE DATABASE Portfolio
GO

-- Connect to SQLite database
:connect /workspace/ravikumar/databases/portfolio.db

