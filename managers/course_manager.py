# managers/course_manager.py

from managers.db_manager import DatabaseManager

class CourseManager:
    def __init__(self):
        self.db = DatabaseManager()

    def create_course(self, name, instructor_id):
        self.db.execute("INSERT INTO courses (name, instructor_id) VALUES (%s, %s)", (name, instructor_id))

    def get_all_courses(self):
        self.db.execute("SELECT * FROM courses")
        return self.db.fetchall()
