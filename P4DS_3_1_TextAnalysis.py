# The task in the course:

# You have been recruited by your friend, a linguistics enthusiast, to create a utility tool
# that can perform analysis on a given piece of text.
# Complete the class 'analysedText' with the following methods -

# Constructor - This method should take the argument text, make it lower case, and remove all punctuation.
# Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?).
# Assign this newly formatted text to a new attribute called fmtText.

# freqAll - This method should create and return dictionary of all unique words in the text,
# along with the number of times they occur in the text.
# Each key in the dictionary should be the unique word appearing in the text
# and the associated value should be the number of times it occurs in the text.
# Create this dictionary from the fmtText attribute.

# freqOf - This method should take a word as an argument and return the number of occurrences of that word in fmtText.

class analysedText(object):

    def __init__(self, text):

        # TODO: Remove the punctuation from <text> and make it lower case.
        chars_to_be_replaced = ['.', '!', ',', '?']
        text = text.lower()

        for char in chars_to_be_replaced:
            text = text.replace(char, '')

        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = text

    def freqAll(self):

        # TODO: Split the text into a list of words
        wordlist = self.fmtText.split(' ')

        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        worddict = {}
        for word in set(wordlist):
            if word not in worddict:
                worddict[word] = wordlist.count(word)

        return worddict

    def freqOf(self, word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0