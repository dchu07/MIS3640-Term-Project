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
    worddict = (process_file())
    try:
        urls = urlopen("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={word_id}").read().decode('utf-8').split()
        for url in urls:
            try:
                data = urlopen(url).read()
                return data
            except HTTPError as e:
                continue
    except HTTPError as e:
        word_id, word = random.choice(list(worddict.items()))
        return retrieve_image(word_id)


def crop_image(url):
    image = Image.open(urllib.request.urlopen(url))
    width, height = image.size

    # below metrics subject to change
    left = width/3
    top = height/3
    right = width/3
    bottom = height/3
    image_2 = image.crop((left, top, right, bottom))
    image_2.show()


def main():
    worddict = (process_file())
    glossdict = (process_glossfile())
    word_id, word = get_random_word(worddict)
    print(word_id, word)
    definition = get_gloss(glossdict, word_id)
    url = retrieve_image(word_id)
    print(url)
    crop_image(url)


if __name__ == '__main__':
    main()
