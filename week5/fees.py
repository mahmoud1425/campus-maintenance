"""Calculate student fees using refactored fee rules."""

from dataclasses import dataclass
from enum import Enum

COURSE_RATE = 350
STAFF_CHILD_RATE = 0.5
SCHOLARSHIP_RATE = 0
SUMMER_FEE = 150
HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_DISCOUNT = 200


class StudentType(Enum):
    """Available student categories."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass
class Course:
    """Represent a course by its credit hours."""

    hours: int


RATES = {
    StudentType.REGULAR: COURSE_RATE,
    StudentType.STAFF_CHILD: COURSE_RATE * STAFF_CHILD_RATE,
    StudentType.SCHOLARSHIP: SCHOLARSHIP_RATE,
}


def tuition_fee(courses, student_type, summer=False, discount=0, extras=()):
    """Calculate the total tuition fee for a student."""
    total = sum(course.hours * RATES[student_type] for course in courses)

    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_DISCOUNT

    if summer:
        total += SUMMER_FEE

    total -= discount
    total += sum(extras)

    return total


def report(courses, student_type, summer=False, discount=0, extras=()):
    """Return a text report containing the calculated fee."""
    fee = tuition_fee(courses, student_type, summer, discount, extras)

    if student_type == StudentType.REGULAR:
        message = f"Student fee: {fee}"
    elif student_type == StudentType.STAFF_CHILD:
        message = f"Staff child fee: {fee}"
    else:
        message = f"Scholarship fee: {fee}"

    if fee > HIGH_FEE_THRESHOLD:
        message += "\nHigh fee"

    return message


def process_all(students):
    """Calculate and return fees for all students."""
    results = {}

    for student in students:
        student_type = StudentType(student["type"])
        fee = tuition_fee(
            student["courses"],
            student_type,
            student["summer"],
        )
        results[student["name"]] = fee

    return results
