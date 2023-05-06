import tkinter as tk
from transformers import pipeline, AutoTokenizer
import sqlite3

# load the model and tokenizer
model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")

# create the Tkinter GUI
root = tk.Tk()

# add a label for the question input field
tk.Label(root, text="Ask a question:").grid(row=0)

# add a text input field for the question
question_input = tk.Entry(root, width=50)
question_input.grid(row=0, column=1)

# add a label for the answer output
tk.Label(root, text="Answer:").grid(row=1)

# add a text output field for the answer
answer_output = tk.Text(root, width=50, height=10)
answer_output.grid(row=1, column=1)

# add a label for the information input field
tk.Label(root, text="Additional information:").grid(row=2)

# add a text input field for the additional information
info_input = tk.Entry(root, width=50)
info_input.grid(row=2, column=1)

# define a function for handling the question input and generating an answer
def generate_answer():
    # get the question from the input field
    question = question_input.get()

    # connect to the database and check if the question has already been taught to the AI
    conn = sqlite3.connect("blog_posts.db")
    c = conn.cursor()
    c.execute("SELECT answer FROM ai_answers WHERE question=?", (question,))
    rows = c.fetchall()

    # if the question has already been taught to the AI, retrieve the answer from the database
    if len(rows) > 0:
        answer_output.delete("1.0", tk.END)
        answer_output.insert(tk.END, rows[0][0])
    else:
        # connect to the database and retrieve the reprocessed_text from the blog_posts table
        c.execute("SELECT reprocessed_text FROM blog_posts")
        rows = c.fetchall()
        text = ""
        for row in rows:
            text += row[0] + " "

        # add the additional information to the text
        info = info_input.get()
        text += info

        # use the model to generate an answer to the question
        answer = model(question=question, context=text)

        # insert the answer into the output field
        answer_output.delete("1.0", tk.END)
        answer_output.insert(tk.END, answer["answer"])

        # save the question and answer to the ai_answers table in the database
        if info:
            c.execute("INSERT INTO ai_answers (question, answer) VALUES (?, ?)", (question, answer["answer"]))
            conn.commit()

    # close the database connection
    conn.close()

# add a button for generating the answer
tk.Button(root, text="Generate Answer", command=generate_answer).grid(row=3, column=1)

# start the Tkinter event loop
root.mainloop()
