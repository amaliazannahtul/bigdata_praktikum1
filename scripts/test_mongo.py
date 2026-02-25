from pymongo import MongoClient

uri = "mongodb+srv://userbigdata:bigdata123@cluster0.blerzyd.mongodb.net/?appName=Cluster0"
try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)