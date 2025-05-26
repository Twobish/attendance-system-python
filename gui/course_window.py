from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QListWidget
from managers.course_manager import CourseManager

class CourseWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Course Management")
        self.setFixedSize(400, 300)

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Course Name")

        self.instructor_id_input = QLineEdit()
        self.instructor_id_input.setPlaceholderText("Instructor ID")

        self.create_button = QPushButton("Create Course")
        self.create_button.clicked.connect(self.create_course)

        self.course_list = QListWidget()

        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.instructor_id_input)
        self.layout.addWidget(self.create_button)
        self.layout.addWidget(self.course_list)

        self.setLayout(self.layout)
        self.load_courses()

    def create_course(self):
        name = self.name_input.text()
        instructor_id = self.instructor_id_input.text()

        if not all([name, instructor_id]):
            QMessageBox.warning(self, "Error", "Fill in both fields.")
            return

        manager = CourseManager()
        try:
            manager.create_course(name, instructor_id)
            QMessageBox.information(self, "Success", "Course created.")
            self.load_courses()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def load_courses(self):
        self.course_list.clear()
        manager = CourseManager()
        courses = manager.get_all_courses()
        for course in courses:
            self.course_list.addItem(f"{course[0]} - {course[1]} (Instructor ID: {course[2]})")
