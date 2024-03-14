from db import db
class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    user_role = db.Column(db.String(50), unique=False, nullable=False)
    registration_date = db.Column(db.Date(), unique=False, nullable=False)
    user_email = db.Column(db.String(70), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), unique=False, nullable=False)