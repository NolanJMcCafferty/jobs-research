import string;

translator = str.maketrans('', '', string.punctuation)

doc = []
docs = []
lines = ''
with open('alljobs.txt', 'r') as rf:
		for line in rf:
			newline = line.translate(translator)
			newline = newline.lower()
			if newline == 'zzz\n':
				doc = lines.split()
				docs.append(doc)
				lines = ''
			else:
				lines = lines+' '+newline 


