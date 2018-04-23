# Characterize Jobs Using Deep Learning

Multi step research project with the ultimate goal of using deep learning methods to better understand the characteristics of different occupations and group jobs together based on the tasks and skills they require.

## Step 1:
   ### Scraping job data.

Initial scraping done on Indeed.com using the script `indeed.py` gathered almost 15000 jobs postings. Includes the title, location, and summary for each job. The file `indeed_jobs.txt` contains a small subset of the postings gathered. Each job posting has a title, location, and sumamry in the text file. 


## Step 2:
   ### Use Doc2Vec to vectorize text data. 
   
   The preparation done on the text data was to remove punctuation and make everything lowercase, done with `prepare.py`. Also, duplicate job postings were removed. 


## Step 3: 
   ### Cluster text data.


## Step 4: 
   ### Use deep learning techniques to group occupations. 
