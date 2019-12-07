import random 

from PIL import Image
from urllib import request


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
    This function returns a random string from the passed list of strings.
    """
    word_id, word = random.choice(list(worddict.items())) 
    return word_id, word


def get_gloss(glossdict, word_id):
    """
    This function takes the random word chosen and returns the definition of the word from glossdict.
    """
    for key in glossdict:
        if key == word_id:
            return glossdict[key]


def retrieve_image(word_id):
    """
    This function takes the random word and its ID and returns the image url
    """
    url = (f"http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}")
    return url

def main():
    worddict = (process_file())
    glossdict = (process_glossfile())
    word_id, word = get_random_word(worddict)
    definition = get_gloss(glossdict, word_id)
    print (retrieve_image(word_id))


if __name__ == '__main__':
    main()
