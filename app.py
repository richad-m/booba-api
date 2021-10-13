from flask import Flask, render_template
import random
from datas import fetch_datas
from missing_word import hole_in_sentence

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/quote')
def quote():
    db = fetch_datas()
    return random.sample(db, 1)[0]


@app.route('/api/guess')
def guess_the_word():
    db = fetch_datas()
    return hole_in_sentence(random.sample(db, 1)[0]['phrase'])


if __name__ == "__main__":
    app.run(debug=True)
