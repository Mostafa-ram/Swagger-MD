from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import UserModel
from schemas import UserSchema, UserUpdateSchema

api_service_name = "mdOnePlace/api"
blp = Blueprint("User", "user", url_prefix=f'/{api_service_name}', description="User Operations")


# user root
@blp.route('/user')
class UserList(MethodView):

    # Post User Endpoint
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_schema):
        user = UserModel(**user_schema)

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error adding user")

        return user

    # GET All User Endpoint
    @blp.response(201, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()


# user by ID
@blp.route('/user/<int:review_id>')
class User(MethodView):
    # GET User Endpoint || Retrieve by ID
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    # Put User Endpoint
    # @jwt_required()
    @blp.arguments(UserUpdateSchema)
    @blp.response(201, UserSchema)
    def put(self, update_schema, user_id):
        data = UserModel.query.get(user_id)

        if data:
            data.first_name = update_schema["first_name"]
            data.last_name = update_schema["last_name"]
            data.password_hash = update_schema["password_hash"]

        else:
            req_review = UserModel(id=user_id, **update_schema)

        db.session.add(data)
        db.session.commit()

        return data

    # @jwt_required()
    # Delete User Endpoint
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User ID: {user_id} is deleted"}
