import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysql2003.",
            database="attendance_system"
        )
        self.cursor = self.conn.cursor()  # <-- dictionary=True kaldırıldı

    def execute(self, query, values=None):
        print("Executing:", query)
        print("With values:", values)
        self.cursor.execute(query, values)  # <-- or () kaldırıldı
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()
