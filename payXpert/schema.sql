CREATE DATABASE payxpert;
Use payxpert;


-- Employee Table
CREATE TABLE Employee
(
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender CHAR(1),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255),
    Position VARCHAR(100),
    JoiningDate DATE,
    TerminationDate DATE
);

-- Payroll Table
CREATE TABLE Payroll
(
    PayrollID INT PRIMARY KEY,
    EmployeeID INT,
    PayPeriodStartDate DATE,
    PayPeriodEndDate DATE,
    BasicSalary DECIMAL(10, 2),
    OvertimePay DECIMAL(10, 2),
    Deductions DECIMAL(10, 2),
    NetSalary DECIMAL(10, 2),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Tax Table
CREATE TABLE Tax
(
    TaxID INT PRIMARY KEY,
    EmployeeID INT,
    TaxYear INT,
    TaxableIncome DECIMAL(10, 2),
    TaxAmount DECIMAL(10, 2),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- FinancialRecord Table
CREATE TABLE FinancialRecord
(
    RecordID INT PRIMARY KEY,
    EmployeeID INT,
    RecordDate DATE,
    Description VARCHAR(255),
    Amount DECIMAL(10, 2),
    RecordType VARCHAR(50),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);