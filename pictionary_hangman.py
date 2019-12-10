import random 
import requests
from PIL import Image
import urllib.request
from urllib.error import HTTPError
from urllib.request import urlopen


def process_file():
    """
    This function processes the txt of words provided by WordNet into a dictionary
    """
    file = open('goodwords.txt')
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


def get_word_image(word_dict):
    """
    returns a valid image-net url
    """
    while True:
        word_id, word = random.choice(list(word_dict.items()))
        print('Now checking:', word_id, word)
        url = f"http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}"
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            continue
        except Exception as err:
            print(f'Other error occurred: {err}')
            continue
        else:
            print(response.content.decode('utf8'))
            if response.content.decode('utf8') == 'The synset is not ready yet. Please stay tuned!':
                continue
            else:
                url = get_image(word_id)
                if url:
                    print('Success!')
                    break
                else:
                    continue
    return word_id, word, url

# def get_random_word(worddict):
#     """
#     This function tests whether a random word has image urls then returns the word
#     """
#     image_link = None
#     while image_link is None: 
#         try:
#             word_id, word = random.choice(list(worddict.items()))
#             # print(word_id, word)
#             urls = urlopen(f"http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}").read().decode('utf-8').split()
#             # print(urls)
#             for url in urls:
#                 try:
#                     image_link = urlopen(url).read()
#                     # print(image_link)
#                     return word_id, word
#                 except (ValueError, HTTPError) as e:
#                     continue
#         except (ValueError, HTTPError) as e:
#             get_random_word(worddict)


def get_gloss(glossdict, word_id):
    """
    This function takes the random word chosen and returns the definition of the word from glossdict
    """
    for key in glossdict:
        if key == word_id:
            return glossdict[key]


def get_image(word_id):
    """
    gets a working image url to use for the pictionary portion of the game
    """
    urls = urlopen(f"http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}").read().decode('utf-8').split()
    for url in urls:
        print(url)
        if 'baidu' in url:  # many images hosted at baidu.com are not available
            continue
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            continue
        except Exception as err:
            print(f'Other error occurred: {err}')
            continue
        else:
            r = urllib.request.urlopen(url)
            print(r.headers.get_content_maintype())
            if r.headers.get_content_maintype() == 'text':
                continue
            elif r.headers.get_content_maintype() == 'image':
                print('Success!')
                return url
    return None

# def get_image(word_id):
#     """
#     This function takes the word and finds a working image url to use for the pictionary portion of the game
#     """
#     urls = urlopen(f"http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}").read().decode('utf-8').split()
#     for url in urls:
#         try:
#             data = urlopen(url).read()
#             # print(data)
#             return url
#         except HTTPError as e:
#             get_image(word_id)
  

def crop_image(url, word):
    """
    crops the functioning image and crops it into 9 pieces and saves it into a local drive
    """
    image = Image.open(urllib.request.urlopen(url))
    # image.show()
    width, height = image.size
    pieces = 9

    # for loop to save image everytime we crop it

    picture_list = []

    for i in range(1,10):
        left = 0
        top = 0
        right = width*(i/pieces)
        bottom = height*(i/pieces)
        image_cropped = image.crop((left, top, right, bottom))
        image_cropped.save(f'{word}-{i}.jpg')
        address = (f'{word}-{i}.jpg')
        picture_list.append(address)
        # image_cropped.show()
    return picture_list
        

def displayBoard(missedLetters, correctLetters, secretWord):
    """
    displays the pictionary playing board (the letters)
    """
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
    print()


def getGuess(alreadyGuessed):
    """
    Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    """
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        return guess


def playAgain():
    """
    This function returns True if the player wants to play again, otherwise it returns False.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    worddict = process_file()
    glossdict = process_glossfile()

    word_id, word, url = get_word_image(worddict)
    print(word_id, word)

    definition = get_gloss(glossdict, word_id)
    # print(definition)
    
    picture_list = crop_image(url, word)

    name = input("Hello! What is your name? ")
    print (f"Hello {name}, Welcome to Pictionary Hangman!")

    missedLetters = ''
    correctLetters = ''
    secretWord = word
    gameIsDone = False

    while True:    
        displayBoard(missedLetters, correctLetters, secretWord)
        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)
        
        # for address in picture_list:
        #         image = Image.open(address)
        #         image.show()


        if guess in secretWord:
            correctLetters = correctLetters + guess
            # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                print(f'The definition of this word is {definition}')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            for i in range(len(missedLetters),len(missedLetters)+1):
                image = Image.open(f'{word}-{i}.jpg')
                image.show()
                break
            # Check if player has guessed too many times and lost
            if len(missedLetters) == 9:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses! The word was "' + secretWord + '"')                    
                print(f'The definition of this word is {definition}')
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                word_id, word = get_random_word(worddict)
                definition = get_gloss(glossdict, word_id)
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = word
            else:
                break


if __name__ == '__main__':
    main()
