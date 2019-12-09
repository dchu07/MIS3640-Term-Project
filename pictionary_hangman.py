import random 
from PIL import Image
import urllib.request
from urllib.error import HTTPError
from urllib.request import urlopen


def process_file():
    """
    This function processes the txt of words provided by WordNet into a dictionary
    """
    file = open('words.txt')
    worddict = {}
    for line in file:
        line = line.split()
        worddict[line[0]] = line[1]
    return worddict


def process_glossfile():
    """
    This function processes the txt of definitions provided by WordNet into a dictionary
    """
    file = open('gloss.txt')
    glossdict = {}
    for line in file:
        line = line.split()
        id = line[0]
        gloss = ' '.join(line[1:])
        glossdict[id] = gloss
    return glossdict

def get_random_word(worddict):
    """
    This function tests whether a random word has image urls then returns the word
    """
    image_link = None
    while image_link is None: 
        try:
            word_id, word = random.choice(list(worddict.items()))
            # print(word_id, word)
            urls = urlopen(f"http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}").read().decode('utf-8').split()
            # print(urls)
            for url in urls:
                try:
                    image_link = urlopen(url).read()
                    # print(image_link)
                    return word_id, word
                except ValueError as e:
                    continue
        except ValueError as e:
            get_random_word(worddict)


def get_gloss(glossdict, word_id):
    """
    This function takes the random word chosen and returns the definition of the word from glossdict
    """
    for key in glossdict:
        if key == word_id:
            return glossdict[key]


def get_image(word_id):
    """
    This function takes the word and finds a working image url to use for the pictionary portion of the game
    """
    urls = urlopen(f"http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}").read().decode('utf-8').split()
    for url in urls:
        try:
            data = urlopen(url).read()
            # print(data)
            return url
        except HTTPError as e:
            get_image(word_id)
  

def crop_image(url):
    image = Image.open(urllib.request.urlopen(url))
    image.show()
    width, height = image.size
    divided = 3

    # below metrics subject to change
    left = 50   
    top = 50
    right = 150
    bottom = 150

    # left = width/divided
    # top = height/divided
    # right = width/divided
    # bottom = height/divided

    image_2 = image.crop((left, top, right, bottom))
    image_2.show()


# HANGMANPICS = ['''
#    +---+
#    |   |
#        |
#        |  
#        |
#        |
#  =========''', '''

#    +---+
#    |   |
#    O   |
#        |
#        |
#        |
#  =========''', '''

#    +---+
#    |   |
#    O   |
#    |   |
#        |
#        |
#  =========''', '''

#    +---+
#    |   |
#    O   |
#   /|   |
#        |
#        |
#  =========''', '''

#    +---+
#    |   |
#    O   |
#   /|\  |
#        |
#        |
#  =========''', '''

#    +---+
#    |   |
#    O   |
#   /|\  |
#   /    |
#        |
#  =========''', '''

#    +---+
#    |   |
#    O   |
#   /|\  |
#   / \  |
#        |
# =========''']


# def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
#     print(HANGMANPICS[len(missedLetters)])
#     print()

#     print('Missed letters:', end=' ')
#     for letter in missedLetters:
#         print(letter, end=' ')
#     print()

#     blanks = '_' * len(secretWord)

#     for i in range(9): # replace blanks with correctly guessed letters
#         if secretWord[i] in correctLetters:
#             blanks = blanks[:i] + secretWord[i] + blanks[i+1:s]

#     for letter in blanks: # show the secret word with spaces in between each letter
#         print(letter, end=' ')
#     print()


# def getGuess(alreadyGuessed):
#     """
#     Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
#     """
#     while True:
#         print('Guess a letter.')
#         guess = input()
#         guess = guess.lower()
#         if len(guess) != 1:
#             print('Please enter a single letter.')
#         elif guess in alreadyGuessed:
#             print('You have already guessed that letter. Choose again.')
#         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
#             print('Please enter a LETTER.')
#         return guess


# def playAgain():
#     """
#     This function returns True if the player wants to play again, otherwise it returns False.
#     """
#     print('Do you want to play again? (yes or no)')
#     return input().lower().startswith('y')


def main():
    worddict = (process_file())
    glossdict = (process_glossfile())

    word_id, word = get_random_word(worddict)
    print(word_id, word)

    # definition = get_gloss(glossdict, word_id)
    # print(definition)

    url = get_image(word_id)
    


    crop_image(url)

    # name = input("Hello! What is your name? ")
    # print (f"Hello {name}, Welcome to Pictionary Hangman!")

    # missedLetters = ''
    # correctLetters = ''
    # secretWord = word
    # gameIsDone = False

    # while True:
    #     displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    #     # Let the player type in a letter.
    #     guess = getGuess(missedLetters + correctLetters)
        
    #     if guess in secretWord:
    #         correctLetters = correctLetters + guess
        
    #         # Check if the player has won
    #         foundAllLetters = True
    #         for i in range(9):
    #             if secretWord[i] not in correctLetters:
    #                 foundAllLetters = False
    #                 break
    #         if foundAllLetters:
    #             print('Yes! The secret word is "' + secretWord + '"! You have won!')
    #             print(f'The definition of this word is {definition}')
    #             gameIsDone = True
    #     else:
    #         missedLetters = missedLetters + guess

    #         # Check if player has guessed too many times and lost
    #         if len(missedLetters) == 9:
    #             displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    #             print('You have run out of guesses! The word was "' + secretWord + '"')
    #             print(f'The definition of this word is {definition}')
    #             gameIsDone = True

    #     # Ask the player if they want to play again (but only if the game is done).
    #     if gameIsDone:
    #         if playAgain():
    #             word_id, word = get_random_word(worddict)
    #             definition = get_gloss(glossdict, word_id)
    #             missedLetters = ''
    #             correctLetters = ''
    #             gameIsDone = False
    #             secretWord = word
    #         else:
    #             break


if __name__ == '__main__':
    main()
