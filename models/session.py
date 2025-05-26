# models/session.py

class Session:
    def __init__(self, session_id, course_id, date, is_active=True):
        self.session_id = session_id
        self.course_id = course_id
        self.date = date
        self.is_active = is_active

    def __str__(self):
        return f"Session on {self.date} (Course ID: {self.course_id})"
