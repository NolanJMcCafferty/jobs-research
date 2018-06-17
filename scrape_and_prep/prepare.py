import string;

# to remove punctuation
translator = str.maketrans('', '', string.punctuation)

# initialize lists
doc = []
docs = []
lines = ''

# read text from jobs file
with open('alljobs.txt', 'r') as rf:
		for line in rf:
			
			# remove punctuation and make lowercase
			newline = line.translate(translator)
			newline = newline.lower()
			
			# seperate job postings as individual docs
			if newline == 'zzz\n':
				doc = lines.split()
				docs.append(doc)
				lines = ''
			else:
				lines = lines+' '+newline 


