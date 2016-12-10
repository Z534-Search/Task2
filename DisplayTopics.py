from gensim.models import LdaModel
from gensim import corpora

dictionary = corpora.Dictionary.load("DataModels/dictionary.dict")
corpus = corpora.BleiCorpus("DataModels/corpus.mm")
lda = LdaModel.load("DataModels/lda_model_topics.lda")
print lda
print lda.num_topics
print ''
print '$$$$$$$$$$$$$$$$$$'
i = 0
for topic in lda.show_topics(num_topics=60):
    print '#' + str(i) + ': ' + str(topic)
    i += 1
