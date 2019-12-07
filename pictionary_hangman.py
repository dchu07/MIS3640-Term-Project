import random 


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
    word = random.choice(worddict)
    for word_id, gloss in word:
        return word_id, gloss


def main():
    worddict = (processfile())
    glossdict = (process_glossfile())
    


if __name__ == '__main__':
    main()
