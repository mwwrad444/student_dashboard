CREATE DATABASE UniversityDB;
GO

USE UniversityDB;
GO

CREATE TABLE Students (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Score FLOAT NOT NULL
);
GO

CREATE OR ALTER PROCEDURE GetStudentResult
    @StudentName NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT Id, Name, Score
    FROM Students
    WHERE Name LIKE '%' + @StudentName + '%';
END;
GO