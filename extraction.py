# Main imports
from main import spark


# CSV Pathname
data_file = "./data/Estudiantes.csv"

# CSV read
init_dataframe = spark.read.csv(data_file, header=True)

# CSV rows
print("Total Records = {}".format(init_dataframe.count()))

# Showing first 20 rows
init_dataframe.show(5, truncate=False)

# CSV schema
init_dataframe.printSchema()
