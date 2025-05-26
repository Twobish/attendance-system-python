from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QListWidget
from managers.report_manager import ReportManager

class ReportWindow(QDialog):
    def __init__(self, student_id):
        super().__init__()
        self.setWindowTitle("Attendance Report")
        self.setFixedSize(400, 300)

        self.layout = QVBoxLayout()
        self.label = QLabel("Your Attendance History:")
        self.list_widget = QListWidget()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        self.load_report(student_id)

    def load_report(self, student_id):
        manager = ReportManager()
        records = manager.get_attendance_report_for_student(student_id)
        for date, course, status in records:
            self.list_widget.addItem(f"{date} - {course} - {status.upper()}")
