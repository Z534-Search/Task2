from pymongo import MongoClient
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import gensim
from gensim import corpora
from gensim.corpora import BleiCorpus

corpus_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Corpus"]
corpus_cursor = corpus_collection.find()
mycorpus_cursor = corpus_collection.find()
dictionary = corpora.Dictionary(review['words'] for review in corpus_cursor)
dictionary.filter_extremes(keep_n=10000)
dictionary.compactify()
corpora.Dictionary.save(dictionary,"DataModels/dictionary.dict")
ncorpus =[]
i=0
for review in mycorpus_cursor:
    print i
    i+=1
    ncorpus.append(dictionary.doc2bow(review["words"]))
corpora.BleiCorpus.serialize("DataModels/corpus.mm",ncorpus)
dcorpus = corpora.BleiCorpus("DataModels/corpus.mm")
lda = gensim.models.LdaModel(dcorpus, num_topics=60, id2word=dictionary)
lda.save("DataModels/lda_model_topics.lda")
i=0
for topic in lda.show_topics(num_topics=60):
    print '#' + str(i) + ': ' + str(topic)
    i += 1
