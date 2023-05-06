
import os

# set the path to the folder containing the blog post files
folder_path = 'blog_posts'

# get a list of all the files in the folder
files = os.listdir(folder_path)

# filter out any files that are not text files
txt_files = [file for file in files if file.endswith('.txt')]

# read the first 20 text files and process each file
for file_name in txt_files[:20]:
    with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as f:
        text = f.read()
        # do something with the text, such as preprocessing or analysis
        print(text)
