# models/instructor.py

from models.user import User

class Instructor(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, role="instructor")
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)
