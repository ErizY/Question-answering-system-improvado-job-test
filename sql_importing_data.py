import os
import sqlite3

# create a connection to the database
conn = sqlite3.connect('blog_posts.db')
cursor = conn.cursor()



# set the path to the folder containing the text files
folder_path = 'blog_posts'

# get a list of all the files in the folder
files = os.listdir(folder_path)

# filter out any files that are not text files
txt_files = [file for file in files if file.endswith('.txt')]

# loop through the list of text files and insert each file into the database
for i, file_name in enumerate(txt_files):
    with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as f:
        content = f.read()
        # insert the file into the database
        cursor.execute('''INSERT INTO blog_posts (name, content)
                          VALUES (?, ?)''', (file_name, content))
        # commit the changes
        conn.commit()

# close the connection to the database
conn.close()
