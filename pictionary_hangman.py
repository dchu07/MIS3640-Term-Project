import random

def processfile():
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


def join_file_glossfile(worddict, glossdict):
    """
    This function will join the word dict with the gloss dict
    """
    ds = [worddict, glossdict]
    dict = {}
    for key in worddict.items():
        dict[key] = tuple(dict[key] for dict in ds)



# def getRandomWord(wordList):
#     """
#     This function returns a random string from the passed list of strings.
#     """
#     wordIndex = random.randint(0, len(wordList) - 1)
#     return wordList[wordIndex]


def main():
    worddict = (processfile())
    glossdict = (process_glossfile())
    print(join_file_glossfile(worddict, glossdict))


if __name__ == '__main__':
    main()
