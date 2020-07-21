# Letter Frequency
# 
# Description: Calculates the frequency of each letter
# in a string of text
#
# Input
#   text: string to be analysed
# 
# Output
#   frequency: dictionary with frequency of each letter
#

def analyse_frequency(text):
    alphabet = { 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, "w": 0, 'x': 0, 'y': 0, 'z': 0 }

    for letter in text.lower():
        if letter in alphabet:
            alphabet[letter] += 1

    frequency = sorted(alphabet.items())

    return frequency
