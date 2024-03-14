from db import db
class PatientModel(db.Model):
    __tablename__ = "patientProfile"

    id = db.Column(db.Integer, primary_key=True)
    date_of_birth = db.Column(db.Integer(), unique=False, nullable=False)
    gender = db.Column(db.String(10), unique=False, nullable=False)
    phone = db.Column(db.Integer(), unique=True, nullable=False)
    address = db.Column(db.String(250), unique=False, nullable=False)
