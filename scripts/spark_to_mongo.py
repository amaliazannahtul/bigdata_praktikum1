from pyspark.sql import SparkSession
from pymongo import MongoClient

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("SparkToMongo") \
    .getOrCreate()

data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

df = spark.createDataFrame(data, columns)

result = df.groupBy("category").sum("value")
result.show()

uri = "mongodb+srv://userbigdata:mongo12345@cluster0.blerzyd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client["bigdata_db"]
collection = db["spark_results"]

for row in result.collect():
    collection.insert_one({
        "category": row["category"],
        "total_value": row["sum(value)"]
    })

print("Data berhasil disimpan ke MongoDB Atlas")

spark.stop()