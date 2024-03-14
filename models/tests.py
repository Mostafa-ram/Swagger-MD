from db import db
class TestsModel(db.Model):
    __tablename__ = "tests"

    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    recommended_interval = db.Column(db.String(50), unique=False, nullable=False)