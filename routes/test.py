from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TestsModel
from schemas import TestSchema, TestUpdateSchema

api_service_name = "mdOnePlace/api"
blp = Blueprint("Tests", "tests", url_prefix=f'/{api_service_name}', description="Tests Operations")


# test root
@blp.route('/tests')
class UserList(MethodView):

    # Post test Endpoint
    @blp.arguments(TestSchema)
    @blp.response(201, TestSchema)
    def post(self, user_schema):
        test = TestsModel(**user_schema)

        try:
            db.session.add(test)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error adding test")

        return test

    # GET All test Endpoint || Retrieve all
    @blp.response(201, TestSchema(many=True))
    def get(self):
        return TestsModel.query.all()


# test by ID
@blp.route('/tests/<int:review_id>')
class test(MethodView):
    # GET test Endpoint || Retrieve by ID
    @blp.response(200, TestSchema)
    def get(self, test_id):
        test = TestsModel.query.get_or_404(test_id)
        return test

    # Put test Endpoint
    # @jwt_required()
    @blp.arguments(TestUpdateSchema)
    @blp.response(201, TestSchema)
    def put(self, update_schema, test_id):
        data = TestsModel.query.get(test_id)

        if data:
            data.review = update_schema["review"]
            data.rating = update_schema["rating"]
        else:
            req_review = TestsModel(id=test_id, **update_schema)

        db.session.add(data)
        db.session.commit()

        return data

    # @jwt_required()
    # Delete test Endpoint || Delete
    def delete(self, test_id):
        test = TestsModel.query.get_or_404(test_id)
        db.session.delete(test)
        db.session.commit()
        return {"message": f"test ID: {test_id} is deleted"}
