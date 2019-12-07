import random
import urllib.request

def processfile(file_link):
    """
    This function processes the list of words provided by WordNet
    """
    file = urllib.request.urlopen(file_link)
    wordDict = {}
    for line in file:
        word = line.strip()
        wordList.append(word)
    return wordList


# def getRandomWord(wordList):
#     """
#     This function returns a random string from the passed list of strings.
#     """
#     wordIndex = random.randint(0, len(wordList) - 1)
#     return wordList[wordIndex]


def main():
    print (processfile("http://image-net.org/archive/words.txt"))


if __name__ == '__main__':
    main()