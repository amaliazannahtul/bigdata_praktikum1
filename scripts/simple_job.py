from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SimpleJob") \
    .config("spark.sql.shuffle.partitions", "1") \
    .config("spark.ui.showConsoleProgress", "false") \
    .getOrCreate()

data = [("A", 10), ("B", 20), ("A", 30)]

df = spark.createDataFrame(data, ["category", "value"])

df.groupBy("category").sum("value").show()

spark.stop()