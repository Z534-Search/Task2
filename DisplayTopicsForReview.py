from pymongo import MongoClient
from gensim.models import LdaModel
from gensim import corpora

dictionary = corpora.Dictionary.load("DataModels/dictionary.dict")
corpus = corpora.BleiCorpus("DataModels/corpus.mm")
lda = LdaModel.load("DataModels/lda_model_topics.lda")

corpus_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Corpus"]

i=0
corpus_cursor = corpus_collection.find()
for review in corpus_cursor:
             # assume there's one document per line, tokens separated by whitespace
             i=i+1
             print lda[dictionary.doc2bow(review["words"])]
             if i ==20:
                 break;
