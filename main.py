# TODO: Quitar el guión en el campo srtCedula [X]
# TODO: Capitalizar 3 columnas strNombres, srtApellidos y srtNacionalidad [X]
# TODO: Las otras columnas deben ser eliminadas del dataset nuevo. [X]

# PySpark imports
import findspark
from pyspark.sql import SparkSession


# Initialize Spark Session
findspark.init()

# Set Spark Session
spark = (
    # Session name
    SparkSession.builder.appName("EncuestaHabilidadesDigitalesMintel")
    # How many PC cores Spark will use for the session
    .config("spark.sql.shuffle.partitions", "4")
    # Create session or get if it is already created
    .getOrCreate()
)
