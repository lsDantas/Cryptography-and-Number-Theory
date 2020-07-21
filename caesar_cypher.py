# Caesar Cypher
#
# Description: Encode and decode a string of text
# using the Caesar rotation cypher.
#
# Input
#   text: a string of text to be used
#   rot:  rotation 
#
# Output 
#   encoded: string encoded using Caesar cypher
#   decoded: string decoded using Caesar cypher
#

def encode(text, rot):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    encoded = ""

    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter) + rot
            if position >= 26:
                position -= 26
            encoded += alphabet[position]

        else:
            encoded += letter

    return encoded

def decode(text, rot):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    decoded = ""

    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter) - rot
            if position < 0:
                position += 26
            decoded += alphabet[position]
        else:
            decoded += letter

    return decoded