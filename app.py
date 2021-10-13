from flask import Flask
import random
from datas import fetch_datas
from missing_word import hole_in_sentence

app = Flask(__name__)


@app.route('/api/quote')
def quote():
    db = fetch_datas()
    return random.sample(db, 1)[0]


@app.route('/api/guess')
def guess_the_word():
    db = fetch_datas()
    return hole_in_sentence(random.sample(db, 1)[0]['phrase'])
