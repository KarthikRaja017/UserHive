from dotenv import load_dotenv
import os
load_dotenv() 


config = os.environ
DB_NAME = config.get("DB_NAME", "")

MONGO_URI = config.get("LOCAL_MONGO_URI", "")
MONGO_DATABASE = DB_NAME