from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TestResultsModel
from schemas import ResultsSchema, ResultsUpdateSchema
api_service_name = "mdOnePlace/api"
blp = Blueprint("Results", "results", url_prefix=f'/{api_service_name}', description="Results Operations")


# results root
@blp.route('/results')
class ResultsList(MethodView):

    # Post..Create New
    @blp.arguments(ResultsSchema)
    @blp.response(201, ResultsSchema)
    def post(self, results_schema):
        result = TestResultsModel(**results_schema)

        try:
            db.session.add(result)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error adding result")

        return result

    # GET All Result Endpoint
    @blp.response(201, ResultsSchema(many=True))
    def get(self):
        return TestResultsModel.query.all()


# result by ID
@blp.route('/results/<int:review_id>')
class Results(MethodView):
    # GET Result Endpoint || Retrieve by ID
    @blp.response(200, ResultsSchema)
    def get(self, result_id):
        result = TestResultsModel.query.get_or_404(result_id)
        return result

    # Update if exists and create if new
    # @jwt_required()
    @blp.arguments(ResultsUpdateSchema)
    @blp.response(201, ResultsSchema)
    def put(self, update_schema, result_id):
        data = TestResultsModel.query.get(result_id)

        if data:
            data.review = update_schema["date_taken"]
            data.rating = update_schema["status"]
        else:
            req_review = TestResultsModel(id=result_id, **update_schema)

        db.session.add(data)
        db.session.commit()

        return data

    # @jwt_required()
    # Delete Result Endpoint
    def delete(self, result_id):
        result = TestResultsModel.query.get_or_404(result_id)
        db.session.delete(result)
        db.session.commit()
        return {"message": f"Result ID: {result_id} is deleted"}
