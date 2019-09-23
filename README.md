# Characterize Jobs Using Deep Learning

Multi step research project with the ultimate goal of using deep learning methods to better understand the characteristics of different occupations and group jobs together based on the tasks and skills they require.

## Step 1:
   ### Scraping job data.

Initial scraping done on Indeed.com using the script `indeed.py` gathered almost 30000 jobs postings. Includes the title, location, and summary for each job. The file `indeed_jobs.txt` contains a small subset of the postings gathered. Each job posting has a title, location, and sumamry in the text file. These files are in the `scrape_and_prep` directory.


## Step 2:
   ### Use Doc2Vec to vectorize text data. 
   
The preparation done on the text data was to remove punctuation and make everything lowercase, done with `prepare.py`. Also, duplicate job postings were removed. The initial Doc2Vec notebooks are in the `doc2vec` directory. 


## Step 3: 
   ### Create LDA model for Topic Modeling 
  
LDA model was chosen because the topic vectors would be more interpretable and sparse than Doc2Vec document vectors. The initial LDA notebooks are in the `lda` directory.

## Step 4:
   ### Scale Models for BurningGlass Technologies Dataset

Adapt the previous models to run with hundreds of millions of job postings. These notebooks are in the `BGT` directory and use either 5, 50, or 500 random job postings from each day in the range of our job posting data (because we did not have the computational power to deal with all the documents at once). 
