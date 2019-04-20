#Script reads all files from tier-1, applies required transformations, joins them based on keys, and saves to tier-2
import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, lit, asc
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StructType, StringType, LongType
from pyspark.sql.types import StructField, IntegerType
from pyspark.sql.functions import monotonically_increasing_id, udf, lower
from pyspark.sql.functions import concat, col, lit

#Reading the training csv
train_df = spark.read.option("header", "true").csv("gs://dsp-p4/tier-1/application_train.csv")
train_df.count()
#train has 307,511

#Reading bureau.csv
bureau_df = spark.read.option("header", "true").csv("gs://dsp-p4/tier-1/bureau.csv")


