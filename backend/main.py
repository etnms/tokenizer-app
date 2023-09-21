import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from flask import Flask, request
from flask_cors import CORS, cross_origin
    #nltk.download('punkt') # for tokens
    #nltk.download('averaged_perceptron_tagger') # for tagged tokens

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST'])

def main():
    data = request.form['text']
    print(data)
    sentence = data
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens
    #return tagged_tokens

