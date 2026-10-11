import pyodbc
from config import DB_DRIVER, DB_NAME, DB_SERVER, DB_TRUSTED_CONNECTION


def create_connection():
    """SQL Server ilə əlaqə yaradır."""
    connection_string = (
        f"DRIVER={DB_DRIVER};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"Trusted_Connection={DB_TRUSTED_CONNECTION};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(connection_string, timeout=5)


def add_student(name: str, score: float) -> None:
    """Yeni tələbəni bazaya əlavə edir."""
    query = "INSERT INTO Students (Name, Score) VALUES (?, ?)"
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, score))
            conn.commit()


def get_students() -> list[dict]:
    """Bütün tələbələrin siyahısını qaytarır."""
    query = "SELECT Id, Name, Score FROM Students ORDER BY Id DESC"
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            return [
                {"id": row.Id, "name": row.Name, "score": row.Score}
                for row in rows
            ]


def get_student(name_query: str) -> list[dict]:
    """Ada görə tələbə axtarışı aparır (Stored Procedure istifadə edir)."""
    query = "EXEC GetStudentResult @StudentName = ?"
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name_query,))
            rows = cursor.fetchall()
            return [
                {"id": row.Id, "name": row.Name, "score": row.Score}
                for row in rows
            ]