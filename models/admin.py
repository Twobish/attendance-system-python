# models/admin.py

from models.user import User

class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, role="admin")

    def create_user(self, user):
        # Kullanıcı oluşturma işlemi burada yapılır
        pass
