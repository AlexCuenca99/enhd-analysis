from main import spark

# data_csv = (
#     spark.read.format("csv")
#     .option("header", "true")
#     .option("inferSchema", "true")
#     .option("delimiter", ";")
#     .option("enconding", "latin1")
#     .load("./data/*.csv")
# )
# data_csv.write.parquet("./data/enhd_mintel.parquet")

data_file = "./data/mintel_enhd_2021-da.csv"
sdfData = spark.read.csv(data_file, header=True, sep=";")
print("Total Records = {}".format(sdfData.count()))
sdfData.show(5, truncate=False)
sdfData.printSchema()
