# models/course.py

class Course:
    def __init__(self, course_id, name, instructor_id):
        self.course_id = course_id
        self.name = name
        self.instructor_id = instructor_id  # Foreign key: Instructor ID
        self.sessions = []  # List of Session objects

    def add_session(self, session):
        self.sessions.append(session)

    def __str__(self):
        return f"Course: {self.name} (ID: {self.course_id})"
