import sqlite3
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# download necessary NLTK data
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

# connect to database and retrieve data
conn = sqlite3.connect('blog_posts.db')
c = conn.cursor()
c.execute('SELECT reprocessed_text FROM blog_posts')
data = c.fetchall()

# remove punctuation marks
data = [s[0].translate(str.maketrans('', '', string.punctuation)) for s in data]

# remove stop words
stop_words = set(stopwords.words('english'))
data = [[word for word in word_tokenize(s.lower()) if not word in stop_words] for s in data]

# lemmatize words
lemmatizer = WordNetLemmatizer()
data = [[lemmatizer.lemmatize(word) for word in s] for s in data]

# tokenize text
data = [word_tokenize(' '.join(s)) for s in data]

# print processed data
print(data)
