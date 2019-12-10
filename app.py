from flask import Flask, request, render_template, redirect, url_for, session
from hangman import getGuess, processFile, getRandomWord

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PEPEHANDS'

# @app.route('/')
# def index():
#     """
#     displays index.html as homepage
#     """
#     return render_template('index.html')


@app.route('/', methods = ['POST', 'GET'])
def start():
    """
    Upon clicking the 'Submit' button, the data from the form will be sent via a POST
    request to the Flask backend at the route POST /nearest
    """
    if request.method == 'POST':
        #try:
        session['name'] = request.form['text']
        wordList = processFile()
        session['secretWord'] = getRandomWord(wordList)
        session['guess'] = []
        return redirect(url_for('welcome'))
        #except:
            #return render_template('error.html')
    else:
        return render_template('index.html')

@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    word_len = len(session['secretWord'])
    letter_underscore = '_ ' * word_len
    #guess = getGuess(request.form['text'])
    if request.method == 'POST':
        #return getGuess(request.form['text'])
        return render_template('game_next_letter.html', last_letter = request.form['text'])
    else:
        return render_template('game_start.html', name = session['name'], letter_underscore=letter_underscore, word_len=word_len)
