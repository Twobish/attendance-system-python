# managers/auth_manager.py

from managers.db_manager import DatabaseManager

class AuthManager:
    def __init__(self):
        self.db = DatabaseManager()

    def login(self, email, password):
        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        self.db.execute(query, (email, password))
        user = self.db.fetchone()
        return user  # None dönerse kullanıcı bulunamadı

    def logout(self):
        print("User logged out.")
