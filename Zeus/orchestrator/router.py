from flask import Blueprint

orchestrator_blueprint = Blueprint('orchestrator', __name__)


@orchestrator_blueprint.route("/orchestrator")
def index():
    return 'orchestrator'