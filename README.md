Question-Answering GUI
This is a Python Tkinter GUI application that uses the Hugging Face Transformers library to answer questions based on a corpus of text. It also allows the user to teach the AI answers to new questions.

Installation
Clone the repository to your local machine:


git clone https://github.com/yourusername/question-answering-gui.git

Install the required libraries:

pip install -r requirements.tx

Create a SQLite database file named blog_posts.db in the root directory of the project. This database will store the corpus of text and the AI's learned answers.

Create two tables in the blog_posts.db database:
CREATE TABLE blog_posts (id INTEGER PRIMARY KEY, text TEXT, reprocessed_text TEXT);
CREATE TABLE ai_answers (id INTEGER PRIMARY KEY, question TEXT, answer TEXT);

Run the app.py script:
python app.py


Usage
Ask a question in the "Ask a question:" input field.
Click the "Generate Answer" button to see the AI's answer.
If the AI's answer is incorrect or incomplete, enter the correct answer in the "Additional information:" input field and click the "Generate Answer" button again. The AI will incorporate this new information into its answer and save it to the ai_answers table in the database.
If the AI has not been taught the answer to a question before, it will use the distilbert-base-cased-distilled-squad model to generate an answer based on the corpus of text stored in the blog_posts table.
To exit the application, close the window or press Ctrl+C in the terminal.
Note: This application is just a simple example of how to use the Transformers library for question-answering. It could be extended and improved in many ways, such as by using a larger corpus of text, a more powerful model, or a more sophisticated interface.
