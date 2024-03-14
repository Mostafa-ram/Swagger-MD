from db import db

class AppointmentsModel(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True, nullable=False)
    test_id = db.Column(db.Integer, unique=False, nullable=False)
    appointment_date = db.Column(db.String(50), unique=False, nullable=False)
    status = db.Column(db.String(15), unique=True, nullable=False)

    #relations ..
