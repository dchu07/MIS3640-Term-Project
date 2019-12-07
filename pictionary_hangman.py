import random

<<<<<<< HEAD
def processfile():
=======
def processfile(word_link, def_link):
>>>>>>> 3bac74aa3322806ecf5d1452e73c1f72de6f855e
    """
    This function processes the list of words provided by WordNet
    """
    file = open('words.txt')
    worddict = {}
    for line in file:
        line = line.split()
        worddict[line[0]] = line[1]
    return worddict


<<<<<<< HEAD
def process_glossfile():
    file = open('gloss.txt')
    glossdict = {}
    for line in file:
        line = line.split()
        id = line[0]
        gloss = ' '.join(line[1:])
        glossdict[id] = gloss
    return glossdict









=======
>>>>>>> 3bac74aa3322806ecf5d1452e73c1f72de6f855e
# def getRandomWord(wordList):
#     """
#     This function returns a random string from the passed list of strings.
#     """
#     wordIndex = random.randint(0, len(wordList) - 1)
#     return wordList[wordIndex]


def main():
    # print (processfile('words.txt'))
    # print(process_glossfile())


if __name__ == '__main__':
    main()
