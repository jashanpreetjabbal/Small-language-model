import random
from collections import defaultdict
import re
from pprint import pprint

def load_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_text(text):
    words = text.split()
    word_pairs = [(words[i], words[i+1]) for i in range(len(words)-2)]
    word_dict = defaultdict(list)
    for pair, next_word in zip(word_pairs, words[2:]):
        word_dict[pair].append(next_word)
    return word_dict

def predict_next_word(word_dict, starting_pair=None):
    if starting_pair is None:
        starting_pair = select_starting_pair(word_dict)
    output = list(starting_pair)
    while True:
        next_words = word_dict[starting_pair]
        next_word = random.choice(next_words)
        output.append(next_word)
        if (starting_pair[1], next_word) in word_dict:
            starting_pair = (starting_pair[1], next_word)
        else: 
            break
    return ' '.join(output)
  
def select_starting_pair(word_dict):
    capital_keys = [key for key in word_dict.keys() if key[0][0].isupper()]
    if capital_keys:
        return random.choice(capital_keys)
    else:
        return random.choice(list(word_dict.keys()))
def predict_next_n_words(word_dict, n, starting_pair=None):
    output = predict_next_word(word_dict, starting_pair).split()
    while len(output) < n:
        if len(output) >= n:
            break
        current_pair = (output[-2], output[-1])
        next_word = random.choice(word_dict[current_pair])
        output.append(next_word)
    return ' '.join(output[:n])
  
def load_input_text(source):
    return load_text_from_file(source)

source = 'message-2.txt' 
input_text = load_input_text(source)
parsed_text = parse_text(input_text)
pprint(parsed_text)

predicted_word = predict_next_word(parsed_text)
predicted_text = predict_next_n_words(parsed_text, 100)
print("Predicted Word:", predicted_word)
print("Predicted Text:", predicted_text)
