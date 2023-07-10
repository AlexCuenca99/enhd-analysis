from extraction import *

province = sdfData.groupBy("Provincia:").count()
print(province.show(27, truncate=False))
