
from src.config import MONGO_DATABASE, MONGO_URI

from pymongo import MongoClient
import certifi


class MongoDB:
    def __init__(self, app=None):
        self.client = None
        self.db = None
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.client = MongoClient(MONGO_URI, tlsCAFile=certifi.where()) 
        self.db = self.client[MONGO_DATABASE]

    def initProductionDb(self, uri, db):
        self.productionClient = MongoClient(
            uri, tlsCAFile=certifi.where()
        ) 
        return self.productionClient[db]

    def getDb(self, dbName):
        return self.client[dbName]


mongo = MongoDB()

