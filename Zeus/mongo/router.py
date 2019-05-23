from flask import Blueprint
mongo_blueprint = Blueprint('mongo', __name__)


@mongo_blueprint.route("/mongo")
def index():
    return 'mongo'