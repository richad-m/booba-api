from flask import Flask
import random
from datas import db
from missing_word import hole_in_sentence

app = Flask(__name__)


@app.route('/quote')
def quote():
    return random.sample(db, 1)[0]


@app.route('/guess')
def guess_the_word():
    return hole_in_sentence(random.sample(db, 1)[0]['phrase'])
