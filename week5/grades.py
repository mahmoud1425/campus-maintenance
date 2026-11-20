"""Grade calculation kata."""

MIN_SCORE = 0
MAX_SCORE = 100

A_GRADE_MIN = 90
B_GRADE_MIN = 80
C_GRADE_MIN = 70
D_GRADE_MIN = 60


def letter_grade(score):
    """Return the letter grade for a numeric score from 0 to 100."""
    if score < MIN_SCORE or score > MAX_SCORE:
        raise ValueError("Score must be between 0 and 100")

    if score >= A_GRADE_MIN:
        return "A"
    if score >= B_GRADE_MIN:
        return "B"
    if score >= C_GRADE_MIN:
        return "C"
    if score >= D_GRADE_MIN:
        return "D"
    return "F"
