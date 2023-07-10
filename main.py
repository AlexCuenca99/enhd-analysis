import findspark
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

findspark.init()

spark = (
    SparkSession.builder.appName("EncuestaHabilidadesDigitalesMintel")
    .config("spark.sql.shuffle.partitions", "4")
    .getOrCreate()
)
