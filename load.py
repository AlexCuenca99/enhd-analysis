from transformation import *


df_ended.show(20, truncate=False)

# CSV schema
df_ended.printSchema()


# Export end dataframe to CSV
df_ended.write.csv("./data/estudiantes_cleaned.csv", header=True, mode="overwrite")
