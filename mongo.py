import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
client = pymongo.MongoClient(MONGO_DB_URL)

print("Databases:", client.list_database_names())

db = client["AMITAI"]   # check if this actually exists
print("Collections in AmitAI:", db.list_collection_names())

# if 'NetworkData' exists, show how many docs
if "NetworkData" in db.list_collection_names():
    print("Documents in NetworkData:", db["NetworkData"].count_documents({}))
    print("First doc:", db["NetworkData"].find_one())
