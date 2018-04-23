import string;
from gensim.models import doc2vec
from collections import namedtuple

translator = str.maketrans('', '', string.punctuation)

docs = []
lines = ''
i = 0

#analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')

with open('alljobs.txt', 'r') as rf:
		for line in rf:
			newline = line.translate(translator)
			newline = newline.lower()
			if newline == 'zzz\n':
				i+=1
				#tags = [i]
				words = lines.split()
				docs.append(words)
				lines = ''
			else:
				lines = lines+' '+newline 




print(len(docs))

# train the model
theModel = doc2vec.Doc2Vec(docs, vector_size=100, window=8, min_count=1, workers=4, alpha=0.025, min_alpha=0.01)

# get the vectors
print(theModel.docvecs[1])
docvec1 = theModel.docvecs[1]

docsim1 = theModel.docvecs.most_similar(1)



