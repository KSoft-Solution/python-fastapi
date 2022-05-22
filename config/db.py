from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://ASHOK:ASHOK@cluster0.lgtry.mongodb.net/?retryWrites=true&w=majority"
# set a 5-second connection timeout
conn = MongoClient(conn_str, server_api=ServerApi('1'),serverSelectionTimeoutMS=5000)

database = conn.users
user_collection = database.get_collection("user")

try:
    print('database connected successfully')
except Exception:
    print("Unable to connect to the server.")
