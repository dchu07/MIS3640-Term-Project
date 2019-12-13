from flask import Flask, request, render_template, redirect, url_for, session
from pictionary_hangman import getGuess, process_file, process_glossfile, get_word_image, get_gloss, crop_image, verifyGuess, guessToString, letterUnderscore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PEPEHANDSLUL'

@app.route('/', methods = ['POST', 'GET'])
def start():
    """
    Upon clicking the 'Submit' button, the data from the form will be sent via a POST
    request to the Flask backend at the route POST /nearest
    """
    session.clear()
    if request.method == 'POST':
        #try:
        session['name'] = request.form['text']
        session['number_incorrect_guesses'] = 0
        session['correct_guess'] = []
        session['incorrect_guess'] = []
        worddict = process_file()
        glossdict = process_glossfile()
        word_id, word, url = get_word_image(worddict)
        session['secretWord'] = word.lower()
        print(session['secretWord'])
        session['definition'] = get_gloss(glossdict, word_id)
        session['picture_list'] = crop_image(url, session['secretWord'])
        return redirect(url_for('welcome'))
        #except:
            #return render_template('error.html')
    else:
        return render_template('index.html')

@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    #guess = getGuess(request.form['text'])
    letter_underscore = "_ " * len(session['secretWord'])
    if request.method == 'POST':
        if len(session['incorrect_guess']) < 9:
            if verifyGuess(request.form['text'], session['incorrect_guess'], session['correct_guess']) == True:
                if request.form['text'] in session['secretWord']:
                    session['correct_guess'] += request.form['text']
                else:
                    session['incorrect_guess'] += request.form['text']
                    if len(session['incorrect_guess']) > 1:
                        session['number_incorrect_guesses'] += 1
                incorrect_guesses = guessToString(session['incorrect_guess'])
                letter_underscore = letterUnderscore(session['secretWord'], session['correct_guess'])
                if ',  '.join(letter_underscore).replace(',','').replace(' ','') == session['secretWord']:
                    session['success1fail0'] = 1
                    return redirect(url_for('end'))
                if request.form['text'] in session['secretWord']:
                    message = 'Correct!'
                    clue_message = ''
                    image_name = 'static/'+session['picture_list'][session['number_incorrect_guesses']]
                    print(image_name)
                    if session['number_incorrect_guesses'] == 0:
                        return render_template('game_next_letter_noimage.html', message = message, incorrect_guesses = incorrect_guesses, last_letter = request.form['text'], letter_underscore = letter_underscore)
                else:
                    clue_message = "Here's a clue:"
                    message = 'Incorrect!'
                    image_name = 'static/'+session['picture_list'][session['number_incorrect_guesses']]
                return render_template('game_next_letter.html', clue_message = clue_message, message = message, incorrect_guesses = incorrect_guesses, last_letter = request.form['text'], letter_underscore = letter_underscore, image_name = image_name)
            else:
                return render_template('game_invalid_letter.html', reason = verifyGuess(request.form['text'], session['incorrect_guess'], session['correct_guess']), last_letter = request.form['text'], letter_underscore = letter_underscore)
        else:
            session['success1fail0'] = 0
            return redirect(url_for('end'))
    else:
        try:
            word_len = len(session['secretWord'])
            letter_underscore = '_ ' * word_len
            return render_template('game_start.html', name = session['name'], letter_underscore=letter_underscore, word_len=word_len)
        except KeyError:
            return redirect(url_for('start'))

@app.route('/end', methods = ['POST', 'GET'])
def end():
    if request.method == 'POST':
        name = session['name']
        if request.form['submit_button'] == 'Yes':
            session.clear()
            return redirect(url_for('start'))
        else:
            session.clear()
            return render_template('ending.html', name=name)
    else:
        try:
            if session['success1fail0'] ==1:
                name = session['name']
                secret_word = session['secretWord']
                definition = session['definition']
                ending_message_1 = f'Congratulations {name}! You guessed the word correctly!'
                ending_message_2 = f'The word was {secret_word}.'
                definition_message= f'{secret_word} means {definition}.'
                return render_template('game_end.html', ending_message_1 = ending_message_1, ending_message_2 = ending_message_2, definition_message = definition_message)
            else:
                name = session['name']
                secret_word = session['secretWord']
                definition = session['definition']
                ending_message_1 = f'Unlucky! {name}, you were not able to guess the word correctly!'
                ending_message_2 = f'The word was {secret_word}.'
                definition_message= f'{secret_word} means {definition}.'
                return render_template('game_end.html', ending_message_1 = ending_message_1, ending_message_2 = ending_message_2, definition_message = definition_message)
        except KeyError:
            return redirect(url_for('start'))
