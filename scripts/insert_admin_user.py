import os

import bcrypt
from sqlalchemy import create_engine, text

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///database.db"
admin_username = os.environ.get("ADMIN_USERNAME") or "admin"
admin_password = os.environ.get("ADMIN_PASSWORD") or "admin"
engine = create_engine(DATABASE_URL, echo=True)


def save_admin_user_in_db(user_name, password):
    salt = bcrypt.gensalt(rounds=14)
    hashed_passw = str(bcrypt.hashpw(password.encode('utf-8'), salt))
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO user (username, password) VALUES (:x, :y)"),
            [{"x": user_name, "y": hashed_passw}],
        )
        conn.commit()


save_admin_user_in_db(admin_username, admin_password)
