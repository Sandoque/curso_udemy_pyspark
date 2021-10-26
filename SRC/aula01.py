from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = (SparkSession.builder
             .master("local[3]")
             .appName("estudando-dataframes")
             .getOrCreate())

    df = (spark
          .read
          .format("csv")
          .option("header", "true")
          .option("inferSchema", "true")
          .option("delimiter", ";")
          .load("csv/arquivo_geral.csv"))

    df.show(10)
