import re
from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open("dictionary.txt") as file:
        word_list = file.read().split()
        return word_list
    
def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value=0
    
    value = sum ( LETTER_SCORES.get(char.upper(), 0) for char in word) # dict.get return 0 if key value not found. 
    return value

def max_word_value(word_list = []):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list == [] :
        word_list = load_words() 
    print(word_list)
    return max(word_list, key = calc_word_value)
# word_list is list class, it will send each item as argument to calc_word_value function and stores the value associated by respective item in the list, and once all iterations are over, max will check for max value and returns associated item of the list
# Demo: http://tiny.cc/dncwkz
if __name__ == "__main__":
    print(max_word_value([]))
    #print(load_words())