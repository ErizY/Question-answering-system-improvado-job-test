import sqlite3
from transformers import pipeline

# connect to SQLite database
conn = sqlite3.connect('blog_posts.db')
c = conn.cursor()

# load pre-trained QAS model
qas = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# define function to get answer to question
def get_answer(question):
    # execute SQL query to get data from database
    c.execute("SELECT reprocessed_text FROM blog_posts")
    data = c.fetchall()

    # loop over data to find best answer
    best_answer = ''
    best_score = 0
    for text in data:
        # get answer to question using pre-trained QAS model
        answer = qas({'question': question, 'context': text[0]})
        score = answer['score']
        if score > best_score:
            best_score = score
            best_answer = answer['answer']
    return best_answer

# example usage
question = 'What is the purpose of this dataset?'
answer = get_answer(question)
print(answer)
