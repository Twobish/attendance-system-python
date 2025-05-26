import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='attendance_system',
        user='root',
        password='Mysql2003.'
    )

    if connection.is_connected():
        print("✅ Connection successful.")
        cursor = connection.cursor()

        # Add Irem
        cursor.execute("""
            INSERT INTO users (name, email, password, role)
            VALUES ('Irem', 'irem@example.com', 'password123', 'student')
        """)
        connection.commit()
        print("✅ User 'Irem' added successfully.")

        # Verify insertion
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("👤 Users table contents:")
        for row in rows:
            print(row)

except Error as e:
    print(f"❌ Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔌 MySQL connection is closed.")
