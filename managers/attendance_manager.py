# managers/attendance_manager.py

from managers.db_manager import DatabaseManager

class AttendanceManager:
    def __init__(self):
        self.db = DatabaseManager()

    def mark_attendance(self, session_id, student_id, status):
        self.db.execute("INSERT INTO attendance (session_id, student_id, status) VALUES (%s, %s, %s)",
                        (session_id, student_id, status))

    def get_attendance_by_session(self, session_id):
        self.db.execute("SELECT * FROM attendance WHERE session_id=%s", (session_id,))
        return self.db.fetchall()
