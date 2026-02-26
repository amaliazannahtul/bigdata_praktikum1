from pymongo import MongoClient

uri = "mongodb+srv://userbigdata:mongo12345@cluster0.blerzyd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

print(client.list_database_names())