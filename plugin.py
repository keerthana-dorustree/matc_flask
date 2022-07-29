from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_mongoengine import MongoEngine

import pymysql
from config import Development
from flasgger import Swagger
import logging

pymysql.install_as_MySQLdb()
db = SQLAlchemy()

SWAGGER_TEMPLATE = {
    "tags": {"name": "Employee", "description": "Employee Details"},
    "securityDefinitions": {"Bearer": {"type": "apiKey", "name": "token", "in": "header"}}}


logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


def index(config=Development):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'XYZ@12345'
    swag = Swagger(app, template=SWAGGER_TEMPLATE, )
    app.config.from_object(config)

    # app.config['MONGODB_SETTINGS'] = {
    # 'db': 'flask',
    # 'host': 'localhost',
    # 'port': 27017
    # }
    # db = MongoEngine()
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from app.api import urls
        app.register_blueprint(urls.index)
        db.create_all()
        migrate.init_app(app, db)

    return app
