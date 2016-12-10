import os
import time
import json
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from pymongo import MongoClient

reviews_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Reviews"]
business_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Business"]
corpus_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Corpus"]

stopset = set(stopwords.words('english'))
stopwords = {}
with open('stopwords.txt', 'rU') as f:
    for line in f:
        stopwords[line.strip()] = 1
lmtzr = WordNetLemmatizer()

with open('../yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json') as dataset:
    for line in dataset:
        data = json.loads(line)
        if 'Restaurants' in data["categories"] and data['city'] == 'Phoenix':
            business_collection.insert({"_id": data["business_id"]})

n=0
with open('../yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json') as dataset:
    for line in dataset:
        data = json.loads(line)
        if data["type"] == "review" and business_collection.find({"_id": data["business_id"]}).count() !=0:
            n+=1
            print n
            reviews_collection.insert({
            "reviewId": data["review_id"],
            "business": data["business_id"],
            "text": data["text"],
            "stars": data['stars'],
            "votes":data["votes"]
            })
            words = []
            sentences = nltk.sent_tokenize(data["text"].lower())
            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence)
                filteredWords = [word for word in tokens if word not in stopwords]
                tagged_text = nltk.pos_tag(filteredWords)
                for word, tag in tagged_text:
                    if tag in ['NN','NNS'] :
                        words.append(lmtzr.lemmatize(word))
            corpus_collection.insert({
                  "reviewId": data["review_id"],
                  "business": data["business_id"],
                  "stars": data['stars'],
                  "votes":data["votes"],
                  "text": data["text"],
                  "words": words
            })
