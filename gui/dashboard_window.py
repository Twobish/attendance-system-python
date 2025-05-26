from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout
from gui import ReportWindow
from gui import AttendanceWindow
from gui import CourseWindow

class DashboardWindow(QDialog):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle(f"{user[4].capitalize()} Dashboard")  # role field
        self.setFixedSize(300, 250)

        self.label = QLabel(f"Welcome, {user[1]}!")  # user[1] = name

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        if user[4] == "student":
            report_btn = QPushButton("View Attendance Report")
            report_btn.clicked.connect(self.open_report)
            layout.addWidget(report_btn)

        elif user[4] == "instructor":
            attendance_btn = QPushButton("Manage Attendance")
            attendance_btn.clicked.connect(self.open_attendance)
            layout.addWidget(attendance_btn)

        elif user[4] == "admin":
            course_btn = QPushButton("Manage Courses")
            course_btn.clicked.connect(self.open_course_mgmt)
            layout.addWidget(course_btn)

        self.setLayout(layout)

    def open_report(self):
        win = ReportWindow(self.user[0])  # user_id
        win.exec()

    def open_attendance(self):
        win = AttendanceWindow(self.user[0])
        win.exec()

    def open_course_mgmt(self):
        win = CourseWindow()
        win.exec()
