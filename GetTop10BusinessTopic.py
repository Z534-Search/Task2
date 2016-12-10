import os
import time
import json
from pymongo import MongoClient
from collections import Counter,defaultdict

reviews_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Reviews"]
business_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Business2"]
topic_rating_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["TopicRating"]

def getBest(num):
    count =  Counter();
    ave = Counter();
    res = defaultdict()
    for topic_id in range(60):
        result = topic_rating_collection.find({'ratings.'+str(topic_id):{'$exists':True}})
        temp =0
        for a in result:
             temp = temp + int(a['ratings'][str(topic_id)])
       # print temp
        ave[topic_id] = temp/result.count()
        count[topic_id] = result.count()
    #returns valid collection
    #print count.most_common(5)
    for id in count.most_common(num):
        res[id[0]] = (id[1],ave[id[0]])
    print res

getBest(10)
