# sql.py - Create a SQLite3 table and populate it with data

import sqlite3

# create a new databse if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("CREATE TABLE posts \
        (title TEXT, post TEXT)")

    # insert dummy data into the table
    records = (
        ("good", "I\'m good"),
        ("Well", "I\'m well"),
        ("Excellent", "I'm excellent"),
        ("Okay", "I\'m okay."),
        )
    c.executemany("INSERT INTO posts VALUES(?, ?)", records)
