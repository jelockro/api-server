import os

from flask import Flask
from .mongo.helpers import get_mongo


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        MONGO_DATABASE="localhost",

    )

    mongo = get_mongo()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/pages/<page_name>")
    def page(page_name):
        doc = mongo_client

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from .mongo.flask_mongoalchemy import MongoAlchemy
    with app.app_context():
        mongo = MongoAlchemy()
        mongo.init_app(app)

    # from .mongo import helpers
    # helpers.init_app(app)

    from .mongo.router import mongo_blueprint
    app.register_blueprint(mongo_blueprint)

    from .orchestrator.router import orchestrator_blueprint
    app.register_blueprint(orchestrator_blueprint)
    #
    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    return app