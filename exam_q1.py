import string

def read_file(file_name):
    """
    opens the file and processes the file into a list
    """
    file = open(file_name)
    output = []
    for line in file:
        word = line.strip()
        output.append(word)
    return output


def value_of_word(word):
    """
    takes the word and calculates the values of the word, character by character
    then sums the values of the characters to return the values of the entire word
    """
    input = word.lower()
    result = 0
    for character in input:
        number = ord(character) - 96
        result += number
    return result


def values_of_list(list_of_words):
    """
    takes the list of words, and puts them in the dictionary
    key = word
    values = the total value of the word
    """
    d = {}
    result = 0
    for word in list_of_words:
        result = value_of_word(word)
        d[word] = result
    return d


def most_valuable_name(dict):
    """
    finds the most valuable name by seeing which name has the maximum value in the dictionary of names
    """
    most_valuable = max(dict, key = dict.get)
    return most_valuable


def value_of_most_value_name(dict):
    """
    finds the most value of the most valuable name by seeing which name has the maximum value in the dictionary of names
    """
    most_valuable = max(dict, key = dict.get)
    return dict[most_valuable]


def pos_words_with_same_value(file_pos_words, val):
    """
    reads the file of positive words and creates a dictionary of positive words with the values of those words
    then compares it to a given value, and prints our matching positive words that have the same value
    """
    pos_words = read_file(file_pos_words)
    dict_pos_words = values_of_list(pos_words)
    words = []
    for key, value in dict_pos_words.items(): 
        if val == value: 
           words.append(key)
    return words


def main():
    print("The most valuabe name in MIS3640-Problem Solving and Software Design Class is:")
    roster = read_file("roster.txt")
    dict_roster = values_of_list(roster)

    name = most_valuable_name(dict_roster)
    value = value_of_most_value_name(dict_roster)
    print(f"{name} with {value} as the value of her name.")

    print(f"The positive words that have the same value as Demi are:")
    value_name = value_of_word("Demi")
    print(pos_words_with_same_value("positive-words.txt", value_name))

if __name__ == '__main__':
    main()


