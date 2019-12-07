import random

def processfile(word_link, def_link):
    """
    This function processes the list of words provided by WordNet
    """
    file = open(file_link)
    worddict = {}
    for line in file:
        line = line.split()
        worddict[line[0]] = line[1]
    return worddict


# def getRandomWord(wordList):
#     """
#     This function returns a random string from the passed list of strings.
#     """
#     wordIndex = random.randint(0, len(wordList) - 1)
#     return wordList[wordIndex]


def main():
    print (processfile('words.txt'))


if __name__ == '__main__':
    main()