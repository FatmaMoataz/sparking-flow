from pyspark import SparkSession

spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

text = "Hello world. This is a sample text for word count using PySpark. PySpark is great for big data processing."

words = spark.sparkContext.parallelize(text.split(" "))

word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

for wc in word_counts.collect():
    print(wc[0], wc[1])                       

spark.stop()