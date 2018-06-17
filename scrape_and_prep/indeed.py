import requests
from bs4 import BeautifulSoup

# initialize arrays
summaries = []
titles = []
locations = []

# loop through the first 1000 search results pages
for i in range(1,1000):
	
	# each search page url has a multiple of 10 at the end
	index = str(10*i)
	
	# request the search results page 
	r = requests.get('https://www.indeed.com/jobs?q=&l=United+States&start='+index)
	soup = BeautifulSoup(r.text, 'html.parser')
	
	# loop through each search result (job post) 
	results = soup.find_all('a', attrs={'class':'turnstileLink', 'data-tn-element':'jobTitle'})
	for link in results:
		req = requests.get('https://www.indeed.com/'+link['href'])
		soup = BeautifulSoup(req.text, 'html.parser')
		
		# find the job title
		t = soup.find_all('b', attrs={'class':'jobtitle'})
		titles.append(t[0].text)
		
		# find the location
		l = soup.find_all('span', attrs={'class':'location'})
		locations.append(l[0].text)
		
		# find the job summary
		s = soup.find_all('span', attrs={'class':'summary'})
		summaries.append(s[0].text)

print(len(summaries))

# write the job postings to a text file
f = open('alljobs.txt', 'w')
for j in range(1,len(summaries)):
	f.write(str(titles[j])+'\n')
	f.write(str(locations[j]+'\n'))
	f.write(str(summaries[j])+'\n\n')
f.close()
