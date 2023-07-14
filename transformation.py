# Constants
DEFAULT_APELLIDO = "Desconocido"
DEFAULT_NOMBRE = "Desconocido"

# Extraction imports
from extraction import *
from pyspark.sql.functions import col, initcap, lit, regexp_replace, when

# Deletion of srtFechaNac, strCodeSexo, strCodEstCiv, strCodCiudadProc
columns_to_delete = [
    "dtFechaNac",
    "strCodSexo",
    "strCodEstCiv",
    "strCodCiudadProc",
]

df_dropped_columns = init_dataframe.drop(*columns_to_delete)

# Capitalize strNombres, strApellidos
df_nombres_apellidos = df_dropped_columns.withColumn(
    "strNombresCapitalizados",
    when(col("strNombres").isNull(), DEFAULT_NOMBRE).otherwise(
        initcap(col("strNombres"))
    ),
).withColumn(
    "strApellidosCapitalizados",
    when(col("strApellidos").isNull(), DEFAULT_APELLIDO).otherwise(
        initcap(col("strApellidos"))
    ),
)


# Replace strNacionalidad
df_nacionalidad = df_nombres_apellidos.withColumn("strNacionalidad", lit("Ecuatoriana"))

# Remove hypen from srtCedula
df_cedula = df_nacionalidad.withColumn(
    "srtCedula", regexp_replace(col("strCedula"), "-", "")
)

df_dropped_unused = df_cedula.drop("strCedula").drop("strNombres").drop("srtApellidos")

df_renamed = (
    df_dropped_unused.withColumnRenamed("srtCedula", "Cedula")
    .withColumnRenamed("strNombresCapitalizados", "Nombres")
    .withColumnRenamed("strApellidosCapitalizados", "Apellidos")
    .withColumnRenamed("strNacionalidad", "Nacionalidad")
    .withColumnRenamed("strCedula", "Cedula")
)


# Order columns
NEW_ORDER = ["Cedula", "Nombres", "Apellidos", "Nacionalidad"]

df_ended = df_renamed.select(*NEW_ORDER)
