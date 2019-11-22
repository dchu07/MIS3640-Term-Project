import random

name = input("What is your name? ")
print (f"Hello {name}, Welcome to Hangman!")

def processfile(file_name):
    file = open("words.txt")
    wordList = []
    for line in file:
        word = line.strip()
        wordList.append(word)
    return wordList


def getRandomWord(wordList):
    """
    This function returns a random string from the passed list of strings.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def main():
    processfile("words.txt")


if __name__ == '__main__':
    main()