from flask import Flask, jsonify
from flask_smorest import Api
from flask_migrate import Migrate
from db import db
from routes.patient import blp as PatientBlueprint
from routes.user import blp as UserBlueprint
from routes.test import blp as TestBlueprint
from routes.results import blp as ResultsBlueprint

def create_app():
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "MD API"
    app.config["API_VERSION"] = "v1.0"
    app.config["OPENAPI_VERSION"] = "3.1.0"
    app.config["OPENAPI_URL_PREFIX"] = "/mdOnePlace/api/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123@localhost/testtt"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)
    api.register_blueprint(PatientBlueprint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(TestBlueprint)
    api.register_blueprint(ResultsBlueprint)

    return app

# 1- flask db init
# 2- flask db migrate >> in case edite model db
# 3- flask db upgrade
# 4- flask run