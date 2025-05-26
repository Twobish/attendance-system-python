import threading
from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtCore import QTimer
from managers.user_manager import UserManager

class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setFixedSize(300, 250)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.role_input = QLineEdit()
        self.role_input.setPlaceholderText("Role (student/instructor/admin)")

        self.save_button = QPushButton("Save User")
        self.save_button.clicked.connect(self.handle_save)

        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.role_input)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def handle_save(self):
        thread = threading.Thread(target=self.save_user)
        thread.start()

    def save_user(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.pass_input.text()
        role = self.role_input.text()

        if not all([name, email, password, role]):
            self.safe_call(lambda: QMessageBox.warning(self, "Hata", "Tüm alanları doldur!"))
            return

        try:
            manager = UserManager()
            manager.add_user(name, email, password, role)
            self.safe_call(lambda: QMessageBox.information(self, "Başarılı", "Kullanıcı kaydedildi."))
            self.safe_call(self.close)
        except Exception as e:
            self.safe_call(lambda: QMessageBox.critical(self, "Hata", f"Kayıt başarısız: {e}"))

    def safe_call(self, func):
        QTimer.singleShot(0, func)
