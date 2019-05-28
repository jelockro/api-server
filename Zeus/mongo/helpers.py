from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from flask import current_app, g
import sys, json

class Mongo:
    def __init__(self):
        self.client = self.create_client(current_app.config['MONGO_HOST'])

    def create_client(self, HOST):
        try:
            from urllib.parse import quote_plus
        except ImportError:
            from urllib import quote_plus
        uri = "mongodb://%s:%s@%s" % (
            quote_plus('NetsmartAdmin'), quote_plus('Netsmart99'), HOST)
        try:
            client = MongoClient(uri, 27017)
        except ConnectionFailure:
            print("Server not available")
        return client

    def get_database(self, database_name):
        return self.client[database_name]


def get_mongo():
    if 'mongo' not in g:
        g.mongo = Mongo()
    return g.mongo


def close_mongo(e=None):
    mongo = g.pop('mongo', None)

    if mongo is not None:
        mongo.client.close()
        e = 'status_closed'
    return e

def init_app(app):
    app.teardown_appcontext(close_mongo)