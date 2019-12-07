import random
import urllib.request

def processfile(word_link, def_link):
    """
    This function processes the list of words provided by WordNet
    """
    wordFile = urllib.request.urlopen(word_link)
    defFile = urllib.request.urlopen(def_link)
    wordDict = {}
    defDict = {}
    for line in wordFile:
        word = line.strip()
        (key, val) = word.split()
        wordDict[int(key)] = val
    return wordList


# def getRandomWord(wordList):
#     """
#     This function returns a random string from the passed list of strings.
#     """
#     wordIndex = random.randint(0, len(wordList) - 1)
#     return wordList[wordIndex]


def main():
    print (processfile("http://image-net.org/archive/words.txt", "http://image-net.org/archive/gloss.txt"))


if __name__ == '__main__':
    main()