# models/attendance.py

class Attendance:
    def __init__(self, attendance_id, session_id, student_id, status):
        self.attendance_id = attendance_id
        self.session_id = session_id
        self.student_id = student_id
        self.status = status  # "present" or "absent"

    def __str__(self):
        return f"Student {self.student_id} - {self.status.upper()}"
