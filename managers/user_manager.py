# managers/user_manager.py
from managers.db_manager import DatabaseManager

class UserManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add_user(self, name, email, password, role):
        query = "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)"
        values = (name, email, password, role)

        self.db.execute(query, values)

        # Yeni eklenen kullanıcının id'sini al
        self.db.execute("SELECT LAST_INSERT_ID()")
        user_id = self.db.fetchone()[0]

        # Rol bazlı ek kayıtlar
        if role == "student":
            self.db.execute("INSERT INTO students (id, student_number) VALUES (%s, %s)", (user_id, "S-" + str(user_id)))
        elif role == "instructor":
            self.db.execute("INSERT INTO instructors (id) VALUES (%s)", (user_id,))

        self.db.close()

