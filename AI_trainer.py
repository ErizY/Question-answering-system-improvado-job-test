import tkinter as tk
import sqlite3
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Initialize the NLTK stopwords corpus
#nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("AI Trainer")


# Create a function to train the AI
def train_model():
    # Connect to the SQLite3 database
    conn = sqlite3.connect('blog_posts.db')
    c = conn.cursor()

    # Retrieve the data from the blog_posts table
    c.execute("SELECT reprocessed_text FROM blog_posts")
    data = c.fetchall()

    # Tokenize and preprocess the data
    preprocessed_data = []
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    for post in data:
        tokenized_post = tokenizer.tokenize(post[0])
        filtered_post = [w for w in tokenized_post if not w in stop_words]
        preprocessed_data.append(" ".join(filtered_post))

    # Initialize the BERT model
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    # TODO: Train the model on the preprocessed data

    # TODO: Save the trained model

    # Close the database connection
    conn.close()

    # Display a message box to confirm training is complete
    tk.messagebox.showinfo("Training Complete", "The AI model has been trained on the data from the blog_posts table.")


# Create a button to trigger the training function
train_button = tk.Button(root, text="Train AI", command=train_model)
train_button.pack()

# Start the Tkinter main loop
root.mainloop()
