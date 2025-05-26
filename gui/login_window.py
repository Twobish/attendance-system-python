from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from gui import SignUpWindow

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)

        # Email Label ve LineEdit
        self.label_email = QLabel("Email:")
        self.lineEdit_email = QLineEdit()

        # Password Label ve LineEdit
        self.label_password = QLabel("Password:")
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        # Login Butonu
        self.login_button = QPushButton("Login")

        # Sign Up Butonu
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.open_signup)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_email)
        layout.addWidget(self.lineEdit_email)
        layout.addWidget(self.label_password)
        layout.addWidget(self.lineEdit_password)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

    def open_signup(self):
        self.signup_window = SignUpWindow()
        self.signup_window.exec()
