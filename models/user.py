# models/user.py

class User:
    def __init__(self, user_id, name, email, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role  # "student", "instructor", "admin"

    def __str__(self):
        return f"{self.role.capitalize()}: {self.name} ({self.email})"
