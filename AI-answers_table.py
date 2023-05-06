import sqlite3

# connect to the database
conn = sqlite3.connect('blog_posts.db')
c = conn.cursor()

# create the ai_answers table
c.execute('''CREATE TABLE ai_answers
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              question TEXT NOT NULL,
              answer TEXT NOT NULL)''')

# commit the changes and close the connection
conn.commit()
conn.close()
