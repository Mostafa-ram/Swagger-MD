from db import db
class TestResultsModel(db.Model):
    __tablename__ = "testResults"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, unique=True, nullable=False)
    test_id = db.Column(db.Integer, unique=False, nullable=False)
    date_taken = db.Column(db.String(50), unique=False, nullable=False)
    result_pdf_path = db.Column(db.String(256), unique=False, nullable=False)
    status = db.Column(db.String(15), unique=True, nullable=False)
