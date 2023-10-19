import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.corpus import treebank
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
    #nltk.download('punkt') # for tokens
    #nltk.download('averaged_perceptron_tagger') # for tagged tokens

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST'])

def main():
    data = request.json  # Access the JSON data sent from the frontend
    sentence = data['text']
    type = data['type']
    tokens = word_tokenize(sentence)
    if (type == 'token'):
        return tokens
    if (type == 'tag'):
        tagged_tokens = pos_tag(tokens)
        return tagged_tokens
    if (type == 'stem'):
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in tokens]
        return stemmed_tokens

