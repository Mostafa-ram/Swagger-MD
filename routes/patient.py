from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import PatientModel
from schemas import PatientSchema, PatientUpdateSchema
api_service_name = "mdOnePlace/api"
blp = Blueprint("Patient", "Patient", url_prefix=f'/{api_service_name}', description="Patient Operations")


# Patient root
@blp.route('/patient')
class UserList(MethodView):

    # Post Patient Endpoint || Create New
    @blp.arguments(PatientSchema)
    @blp.response(201, PatientSchema)
    def post(self, user_schema):
        Patient = PatientModel(**user_schema)

        try:
            db.session.add(Patient)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error adding Patient")

        return Patient

    # GET All Patient Endpoint
    @blp.response(201, PatientSchema(many=True))
    def get(self):
        return PatientModel.query.all()


# Patient by ID
@blp.route('/patient/<int:review_id>')
class Patient(MethodView):
    # GET Patient Endpoint... Retrieve by ID
    @blp.response(200, PatientSchema)
    def get(self, user_id):
        Patient = PatientModel.query.get_or_404(user_id)
        return Patient

    # Update if exists and create if new
    # @jwt_required()
    @blp.arguments(PatientUpdateSchema)
    @blp.response(201, PatientSchema)
    def put(self, update_schema, user_id):
        data = PatientModel.query.get(user_id)

        if data:
            data.review = update_schema["review"]
            data.rating = update_schema["rating"]
        else:
            req_review = PatientModel(id=user_id, **update_schema)

        db.session.add(data)
        db.session.commit()

        return data

    # @jwt_required()
    # Delete Patient Endpoint
    def delete(self, user_id):
        Patient = PatientModel.query.get_or_404(user_id)
        db.session.delete(Patient)
        db.session.commit()
        return {"message": f"Patient ID: {user_id} is deleted"}
