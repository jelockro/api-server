from Zeus.mongo.flask_mongoalchemy import MongoAlchemy, BaseQuery
from flask import Flask
from werkzeug.exceptions import NotFound
import pytest


def test_should_provide_all_evolv_clients(app):
    with app.app_context():
        mongo = MongoAlchemy()
