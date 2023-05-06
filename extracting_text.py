import nltk
import sqlite3
from bs4 import BeautifulSoup

# download necessary NLTK data
#.download('punkt')

# create connection to database
conn = sqlite3.connect('blog_posts.db')
cursor = conn.cursor()

# retrieve all records from the blog_posts table
cursor.execute("SELECT * FROM blog_posts")
records = cursor.fetchall()

# loop through each record and extract text from content column
for record in records:
    # remove HTML tags from content column using BeautifulSoup
    soup = BeautifulSoup(record[2], 'html.parser')
    text = soup.get_text()

    # extract text from content column using NLTK
    sentences = nltk.sent_tokenize(text)
    text = '\n'.join(sentences)

    # update the text column with the extracted text
    cursor.execute("UPDATE blog_posts SET text = ? WHERE ID = ?", (text, record[0]))

# commit changes and close the connection
conn.commit()
conn.close()