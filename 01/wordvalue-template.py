from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open('./dictionary.txt') as file:
    	return file.readlines() # readlines will return the content in the list
    pass

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    loadwords = load_words()
    print(loadwords)
