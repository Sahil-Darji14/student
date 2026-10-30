
from fastapi import HTTPException

students = []
next_id = 1


# Create Student
def create_student(student):
    global next_id

    new_student = {
        "id": next_id,
        **student.model_dump()
    }

    students.append(new_student)
    next_id += 1

    return new_student


# Get All Students
def get_all_students():
    return students


# Get Student By ID
def get_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Update Student
def update_student(student_id, student_data):
    for student in students:
        if student["id"] == student_id:
            student.update(student_data.model_dump())
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Delete Student
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
