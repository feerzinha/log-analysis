# Project Log Analysis 
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? 

2. Who are the most popular article authors of all time? 

3. On which days did more than 1% of requests lead to errors? 


## Requirements

##### Database
Download data file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip the folder. The file inside is called `newsdata.sql`.
Create news database using psql and load the data with the command:
`psql -d news -f newsdata.sql`


##### Views
Create the necessary views using the command: 
`psql -d news -f create_views.sql`


## Usage
Execute the `news_report.py` file using python version 2.7

