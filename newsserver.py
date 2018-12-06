#!/usr/bin/env python3

import psycopg2

"""Connect to the news database"""


def connect_to_db():

    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
    except Exception as c:
        print("Failed to connect to the database.")
        return None
    else:
        return c


"""Question 1"""


def articles(db_cursor):
    c.execute("""
            SELECT articles.title, count(*) as num
            FROM   log, articles
            WHERE  log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY num DESC
            LIMIT 3;
    """)
    answer = db_cursor.fetchall()

    print('Three most popular articles of all time')
    print('---------------------------------------')

    for result in answer:
        print('"{title}" - {count} views'
              .format(title=result[0], count=result[1]))
    print()

    return


"""Question 2"""


def authors(db_cursor):
    c.execute("""
            SELECT authors.name, count(*) as num
            FROM   log, articles, authors
            WHERE  log.path = '/article/' || articles.slug
            AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY num DESC;
    """)
    answer = db_cursor.fetchall()

    print('Most popular authors of all time')
    print('--------------------------------')

    for result in answer:
        print('{author} - {count} views'
              .format(author=result[0], count=result[1]))
    print()

    return


"""Question 3"""


def errors(db_cursor):
    c.execute("""
            WITH num_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), num_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT num_requests.day,
                num_errors.count::float / num_requests.count::float * 100
                AS error_pc
                FROM num_requests, num_errors
                WHERE num_requests.day = num_errors.day
              )
            SELECT * FROM error_rate WHERE error_pc > 1;
    """)
    answer = db_cursor.fetchall()

    print('Days with greater than 1% errors')
    print('--------------------------------')

    for result in answer:
        print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
            date=result[0],
            error_rate=result[1]))
    print()

    return


if __name__ == "__main__":
    c = connect_to_db()
    if c:
        articles(c)
        authors(c)
        errors(c)
        c.close()
