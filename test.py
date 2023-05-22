from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("test").setMaster("local")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
print(rdd.count())

