# managers/report_manager.py

from managers.db_manager import DatabaseManager

class ReportManager:
    def __init__(self):
        self.db = DatabaseManager()

    def get_attendance_report_for_student(self, student_id):
        self.db.execute("""
            SELECT s.date, c.name AS course, a.status
            FROM attendance a
            JOIN sessions s ON a.session_id = s.id
            JOIN courses c ON s.course_id = c.id
            WHERE a.student_id = %s
            ORDER BY s.date DESC
        """, (student_id,))
        return self.db.fetchall()
