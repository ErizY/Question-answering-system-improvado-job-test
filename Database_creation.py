import os
import sqlite3

import sqlite3

# create a connection to the SQLite database
conn = sqlite3.connect('blog_posts.db')

# create a cursor object
cursor = conn.cursor()

# execute a CREATE TABLE statement to create the blog_posts table
cursor.execute('''
    CREATE TABLE blog_posts (
        ID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        content TEXT NOT NULL,
        text TEXT,
        reprocessed_text TEXT
    );
''')

# commit the changes and close the connection
conn.commit()
conn.close()
