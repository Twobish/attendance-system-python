# models/student.py

from models.user import User

class Student(User):
    def __init__(self, user_id, name, email, password, student_number):
        super().__init__(user_id, name, email, password, role="student")
        self.student_number = student_number
        self.courses = []  # Liste olarak dersler eklenebilir

    def add_course(self, course):
        self.courses.append(course)
