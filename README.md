# Project Log Analysis 
This project is a log report, it shows the data for three questions, selecting the data from news database.
The three questions are:

1. What are the most popular three articles of all time? Which articles have been accessed the most? 

2. Who are the most popular article authors of all time? 

3. On which days did more than 1% of requests lead to errors? 

For answer this questions, the code build and execute a query using the tables: articles, authors, log and parse the results to show on the report screen. 

## Requirements

##### Database
Download data file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip the folder. The file inside is called `newsdata.sql`.
Create news database using psql and load the data. 
`psql -d news -f newsdata.sql`

##### Views
Create the view named `view_requests_per_day_with_error` to select the number of request grouped by day.
```
create view view_requests_per_day as SELECT date_trunc('day', time) as day, count(time) as num FROM log GROUP BY day
```

Create the view named `view_requests_per_day_with_error` to select the number of request with error grouped by day.
```
create view view_requests_per_day_with_error as SELECT date_trunc('day', time) as day, count(time) as num FROM log WHERE status LIKE '404%' GROUP BY day
```

## Usage
Execute the `news_report.py` file using python version 2.7

