from flask import Flask, render_template
import random
from datas import fetch_datas
from missing_word import hole_in_sentence
from quizz import fetch_quote

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play')
def play():
    # quote_dict = fetch_quote()
    # quote = quote_dict['phrase']
    # song_title = quote_dict['song_title']
    return render_template('play.html')


@app.route('/api/quotes/')
def quote():
    db = fetch_datas()
    return random.sample(db, 1)[0]


@app.route('/api/guess/')
def guess_the_word():
    db = fetch_datas()
    return hole_in_sentence(random.sample(db, 1)[0]['phrase'])


@app.route('/api/quotes/<quote_id>')
def find_quote(quote_id):
    return 'Not implemented yet'


if __name__ == "__main__":
    app.run(debug=True)
