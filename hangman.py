import random

def processFile():
    file = open("words.txt")
    wordList = []
    for line in file:
        word = line.strip()
        wordList.append(word)
    return wordList


def getRandomWord(wordList):
    """
    This function returns a random string from the passed list of strings.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


"""HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()"""


def getGuess(guessed_word):
    """
    Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    """
    guess = str(guessed_word)
    guess = guess.lower()
    #if len(guess) != 1:
        #return render_template('game_next_letter_error.html', error_message = 'Please enter a single letter.')
        #return '<p>Please enter a single letter.</p>'
    #elif guess in alreadyGuessed:
        #return render_template('game_next_letter_error.html', error_message = 'You have already guessed that letter. Choose again.')
        #return '<p>You have already guessed that letter. Choose again.</p>'
    if guess not in 'abcdefghijklmnopqrstuvwxyz':
        #return render_template('game_next_letter_error.html', error_message = 'Please enter a LETTER.')
        return '<p>Please enter a LETTER.</p>'
    else:
        session['guess'].append(guess)
        return render_template('game_next_letter.html', last_letter = guess)


#def playAgain():
    #"""
    #This function returns True if the player wants to play again, otherwise it returns False.
    #"""
    #print('Do you want to play again? (yes or no)')
    #return input().lower().startswith('y')


"""def main():

    words = processfile("words.txt")

    missedLetters = ''
    correctLetters = ''
    sessionsecretWord = getRandomWord(words)

    guess = getGuess(missedLetters + correctLetters)"""

"""        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break"""

if __name__ == '__main__':
    main()
