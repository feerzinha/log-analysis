#!/usr/bin/env python2.7
# coding=utf-8

"""News Report.

This module execute query on database to answer the report questions.

Example:
    For test this, follow README instructions and execute
this file with the command:

        $ python news_report.py

"""

import datetime
import psycopg2

DBNAME = "news"


def get_three_most_popular_articles():
    """Return a String that contains the three most popular articles.

    Answer for this question: What are the most popular
    three articles of all time?
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT a.title, count(l.path) AS access
                 FROM log AS l, articles AS a
                 WHERE l.path LIKE '/article/%' AND
                 l.path = '/article/' || a.slug
                 GROUP BY l.path, a.title ORDER BY access DESC limit 3""")

    data = c.fetchall()
    db.close()

    results = ""

    for name, views in data:
        results += '{} - {} views\n'.format(name, views)

    return results


def get_most_popular_authors():
    """Return a String that contains the most popular article authors.

    Answer for this question: Who are the most popular
    article authors of all time?
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT au.name, count(l.path) AS access
                 FROM log AS l, articles AS a, authors AS au
                 WHERE l.path LIKE '/article/%' AND
                       l.path = '/article/' || a.slug AND
                       a.author = au.id
                 GROUP BY a.author, au.name ORDER BY access DESC""")

    data = c.fetchall()
    db.close()

    results = ""

    for name, views in data:
        results += '{} - {} views\n'.format(name, views)

    return results


def get_days_with_errors():
    """Return the days which had more than 1% of requests lead to errors.

    Return a String that answer the question: On which days did more than 1
    % of requests lead to errors?
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("""SELECT TO_CHAR(ve.day :: DATE, 'Mon dd, yyyy'),
                 cast(ve.num AS decimal(7,2)) / cast(vd.num AS decimal(7,2))
                 FROM view_requests_per_day AS vd,
                 view_requests_per_day_with_error AS ve
                 WHERE vd.day = ve.day AND
                 cast(ve.num AS decimal(7,2)) /
                 cast(vd.num AS decimal(7,2)) > 0.01""")

    data = c.fetchall()
    db.close()

    results = ""

    for day, requests_error in data:
        error = round(requests_error*100, 2)
        results += '{} - {} errors\n'.format(day, error)

    return results


def show_report():
    """Show the answer for this report.

    Answer three question after query data
    """
    print("1. What are the most popular three articles of all time?\n")
    print(get_three_most_popular_articles())
    print("2. Who are the most popular article authors of all time?\n")
    print(get_most_popular_authors())
    print("3. On which days did more than 1% of requests lead to errors?\n")
    print(get_days_with_errors())


if __name__ == "__main__":
    show_report()
