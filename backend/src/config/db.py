
from pymongo import MongoClient
import certifi
from src.config import MONGO_DATABASE, MONGO_URI


class MongoDB:
    def __init__(self, app=None):
        self.client = MongoClient(MONGO_URI, tlsCAFile=certifi.where()) 
        self.db = self.client[MONGO_DATABASE]
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize MongoDB with the given Flask app."""
        self.app = app

    def initProductionDb(self, uri, db):
        """Initialize a production database with a separate URI."""
        production_client = MongoClient(uri, tlsCAFile=certifi.where()) 
        return production_client[db]

    def getDb(self, dbName):
        """Retrieve a specific database by name."""
        return self.client[dbName]


# Initialize the MongoDB connection
mongo = MongoDB()

# Test MongoDB Connection
db = mongo.db  # Default database
print(db.list_collection_names())  # Prints available collections


