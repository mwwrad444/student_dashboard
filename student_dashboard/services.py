from config import (
    GRADE_A,
    GRADE_A_MIN,
    GRADE_B,
    GRADE_B_MIN,
    GRADE_C,
    GRADE_C_MIN,
    GRADE_D,
    GRADE_D_MIN,
    GRADE_F,
)


def calculate_grade(score: float) -> str:
    """Xala əsasən müvafiq Grade-i (A, B, C, D, F) hesablayır."""
    if score >= GRADE_A_MIN:
        return GRADE_A
    elif score >= GRADE_B_MIN:
        return GRADE_B
    elif score >= GRADE_C_MIN:
        return GRADE_C
    elif score >= GRADE_D_MIN:
        return GRADE_D
    return GRADE_F


def calculate_statistics(students: list[dict]) -> dict:
    """Tələbələrin bal statistikalarını (ümumi say, orta, min, max) hesablayır."""
    if not students:
        return {
            "total_students": 0,
            "average_score": 0.0,
            "highest_score": 0,
            "lowest_score": 0,
        }

    scores = [s["score"] for s in students]
    total_students = len(scores)
    average_score = sum(scores) / total_students
    highest_score = max(scores)
    lowest_score = min(scores)

    return {
        "total_students": total_students,
        "average_score": round(average_score, 1),
        "highest_score": highest_score,
        "lowest_score": lowest_score,
    }