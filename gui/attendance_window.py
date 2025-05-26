from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from managers.attendance_manager import AttendanceManager

class AttendanceWindow(QDialog):
    def __init__(self, instructor_id):
        super().__init__()
        self.setWindowTitle("Mark Attendance")
        self.setFixedSize(350, 250)

        self.layout = QVBoxLayout()

        self.session_input = QLineEdit()
        self.session_input.setPlaceholderText("Session ID")

        self.student_input = QLineEdit()
        self.student_input.setPlaceholderText("Student ID")

        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("Status (present/absent)")

        self.mark_button = QPushButton("Mark Attendance")
        self.mark_button.clicked.connect(self.mark_attendance)

        self.layout.addWidget(QLabel("Enter session, student and status:"))
        self.layout.addWidget(self.session_input)
        self.layout.addWidget(self.student_input)
        self.layout.addWidget(self.status_input)
        self.layout.addWidget(self.mark_button)

        self.setLayout(self.layout)

    def mark_attendance(self):
        session_id = self.session_input.text()
        student_id = self.student_input.text()
        status = self.status_input.text()

        if not all([session_id, student_id, status]):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        manager = AttendanceManager()
        try:
            manager.mark_attendance(session_id, student_id, status)
            QMessageBox.information(self, "Success", "Attendance marked successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
