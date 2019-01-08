#!/usr/bin/env python2.7

# coding=utf-8
import datetime
import psycopg2

DBNAME = "news"


def get_three_most_popular_articles():
    """Return a String that contains the three most popular articles

    Answer for this question: What are the most popular
    three articles of all time?
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT a.title, l.path, count(l.path) AS access
                 FROM log AS l, articles AS a
                 WHERE l.path LIKE '/article/%' AND
                 l.path LIKE '%' || a.slug || '%'
                 GROUP BY l.path, a.title ORDER BY access DESC limit 3""")

    data = c.fetchall()
    db.close()

    results = ""

    for article in data:
        name = article[0]
        views = article[2]

        results += "'" + name + "' - " + str(views) + " views \n"

    return results


def get_most_popular_authors():
    """Return a String that contains the most popular article authors

    Answer for this question: Who are the most popular
    article authors of all time?
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT au.name, count(l.path) AS access
                 FROM log AS l, articles AS a, authors AS au
                 WHERE l.path LIKE '/article/%' AND
                       l.path LIKE '%' || a.slug || '%' AND
                       a.author = au.id
                 GROUP BY a.author, au.name ORDER BY access DESC""")

    data = c.fetchall()
    db.close()

    results = ""

    for article in data:
        name = article[0]
        views = article[1]

        results += name + " - " + str(views) + " views \n"

    return results


def get_days_with_errors():
    """Return a String that contains the days which had more
    than 1% of requests lead to errors

    Answer for this question: On which days did more than 1
    % of requests lead to errors?
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("""SELECT ve.day,
                 cast(ve.num AS decimal(7,2)) / cast(vd.num AS decimal(7,2))
                 FROM view_requests_per_day AS vd,
                 view_requests_per_day_with_error AS ve
                 WHERE vd.day = ve.day AND
                 cast(ve.num AS decimal(7,2)) /
                 cast(vd.num AS decimal(7,2)) > 0.01""")

    data = c.fetchall()
    db.close()

    results = ""

    for item in data:
        day_format = str(item[0]).split()
        error = round(item[1], 2)

        results += day_format[0] + " - " + str(error*100) + "% erros \n"

    return results


def show_report():
    print("1. What are the most popular three articles of all time?\n")
    print(get_three_most_popular_articles())
    print("2. Who are the most popular article authors of all time?\n")
    print(get_most_popular_authors())
    print("3. On which days did more than 1% of requests lead to errors?\n")
    print(get_days_with_errors())


if __name__ == "__main__":
    show_report()
