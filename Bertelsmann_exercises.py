# password generator

import random

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

def generate_password():
    keys = random.choices(word_list, k=3)
    password = str(keys[0] + keys[1] + keys[2])
    return password
# It should return a string consisting of three random words 
# concatenated together without spaces

# Now we test the function
password = generate_password()