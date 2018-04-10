import requests
from bs4 import BeautifulSoup


summaries = []
titles = []
locations = []

for w in range(1,5):
	q = 1000*w
	for i in range(q-999,q):
		index = str(10*i)
		r = requests.get('https://www.indeed.com/jobs?q=&l=United+States&start='+index)
		soup = BeautifulSoup(r.text, 'html.parser')
		results = soup.find_all('a', attrs={'class':'turnstileLink', 'data-tn-element':'jobTitle'})
		for link in results:
			req = requests.get('https://www.indeed.com/'+link['href'])
			soup = BeautifulSoup(req.text, 'html.parser')
			t = soup.find_all('b', attrs={'class':'jobtitle'})
			titles.append(t[0].text)
			l = soup.find_all('span', attrs={'class':'location'})
			locations.append(l[0].text)
			s = soup.find_all('span', attrs={'class':'summary'})
			summaries.append(s[0].text)
time.sleep(601)


print(len(summaries))

f = open('alljobs.txt', 'w')
for j in range(1,len(summaries)):
	f.write(str(titles[j])+'\n')
	f.write(str(locations[j]+'\n'))
	f.write(str(summaries[j])+'\n\n ########## \n\n')
f.close()