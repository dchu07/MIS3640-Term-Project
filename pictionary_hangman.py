import random

def processfile():
    """
    This function processes the list of words provided by WordNet
    """
    file = open('words.txt')
    worddict = {}
    for line in file:
        line = line.split()
        worddict[line[0]] = line[1]
    return worddict


def process_glossfile():
    file = open('gloss.txt')
    glossdict = {}
    for line in file:
        line = line.split()
        id = line[0]
        gloss = ' '.join(line[1:])
        glossdict[id] = gloss
    return glossdict









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
