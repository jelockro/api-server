import pytest
import unittest
from mockupdb import go, Command, MockupDB
from pymongo.errors import ConnectionFailure

from Zeus import create_app
from Zeus.mongo.helpers import get_mongo, close_mongo

class MockupDBFlaskTest(unittest.TestCase):
    def setup(self):
        self.server = MockupDB(auto_ismaster=True)
        self.server.run()
        self.app = create_app(self.server.uri).test_client()

    def tearDown(self):
        self.server.stop()

    def test(self):
        future = go(self.app.get, "/pages/my_page_name")
        request = self.server.receives(
            Command('find', 'pages', filter={'name': 'my_page_name'}))
        request.ok(cursor={'id': 0, 'firstBatch': [{'contents':'foo'}]})
        http_response = future()
        self.assertEqual("foo",
                         http_response.get_data(as_text=True))

def test_get_close_db(app, e=None):
    # test the get
    with app.app_context():
        client = get_mongo()
        assert client is get_mongo()
        e = close_mongo()
        assert 'status_closed' in str(e)
        try:
            client.admin.command('ismaster')
        except ConnectionFailure:
            e = "Server not Available"
    assert 'Server not Available' in str(e)
