import random 


def process_file():
    """
    This function processes the list of words provided by WordNet
    """
    file = open('words.txt')
    worddict = {}
    for line in file:
        line = line.split()
        worddict[line[0]] = line[1]
    return worddict


def process_gloss_file():
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
    word = random.choice(worddict)
    for word_id, gloss in word:
        return word_id, gloss


def main():
    # print(processfile('words.txt'))
    # print(process_glossfile())
    worddict = process_file()
    print(get_random_word(worddict))


if __name__ == '__main__':
    main()
