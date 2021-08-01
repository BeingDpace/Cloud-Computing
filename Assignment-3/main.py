from flask import Flask,redirect,render_template,request
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import string
import os

app = Flask(__name__)

def word_count(filename):
    with open(filename, encoding="utf8") as file:
        name=filename
        data = file.read()
        words = data.split()
        total_words = len(words)
    return name, total_words

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/count', methods=['GET'])
def count():
    r1 = word_count("Alice.txt")
    r2 = word_count("CandideEn.txt")
    r3 = word_count("Shakespeare.txt")
    return render_template('count.html', r1=r1, r2=r2, r3=r3)

@app.route('/tokenize', methods=['GET', 'POST'])
def tokenize():
    if request.method == "POST":
        filename = request.form["textfile"]
        file = open(filename, encoding="utf8")
        text = file.read()
        file.close()
        # split into words
        tokens = word_tokenize(text)
        # convert to lower case
        tokens = [w.lower() for w in tokens]
        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        return render_template('tokenize.html', results=words, name=filename)
    return render_template('index.html')
@app.route('/search_word', methods=['GET'])

def search_word():
    filename = request.args.get('textfile')
    word = request.args.get('word')
    results=[]
    fo = open(filename, encoding="utf8")
    line = fo.readline().lower()
    # Initialize counter for line number
    line_no = 1
    # Loop until EOF
    while line != '' :
        # Search for string in line
        index = line.find(word.lower())
        if ( index != -1) :
            results.append([str(line_no),str(index),line])
        # Read next line
        line = fo.readline().lower()
        # Increment line counter
        line_no += 1
    return render_template('search_word.html', results=results, word=word, name=filename)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
