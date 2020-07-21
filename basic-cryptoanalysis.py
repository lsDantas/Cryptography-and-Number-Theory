# Basic Cryptoanalysis
#
# Description: Attempts to crack a piece of text encoded
# with the Caesar cypher.
#
# Input
#   encoded: encoded string of text
# 
# Output
#   reconstructed_phrase: decoded string of text
#

import re, frequency, vocabulary, caesar_cypher

def crack(encoded):

    word_list = vocabulary.load("word-list.txt")

    candidate_phrases = {}

    # Test different rotations
    for rotation in range(1, 26):
        text = caesar_cypher.decode(encoded, rotation)
        identified_words = []

        # Check for presence of each word in list
        for word in word_list:
            if word in text:
                regular_expression = "(^| )" + word + "($| )"
                if re.findall(regular_expression, text):
                    identified_words.append(word)

        # Separate identified words
        if identified_words:
            candidate_phrases[rotation] = set(identified_words)

    # Identify best matching phrase
    max_number_identified_words = 0
    best_rotation = 0
    for identified_rot, words_found in candidate_phrases.items():
        number_letters_decoded = 0
        for decoded_word in words_found:
            number_letters_decoded += len(decoded_word)
        if number_letters_decoded > max_number_identified_words:
            max_number_identified_words = number_letters_decoded
            best_rotation = identified_rot

    # Rebuild Phrase
    reconstructed_phrase = encoded.lower()
    ideal_set = candidate_phrases[best_rotation]
    for plaintext_word in ideal_set:
        encrypted_word = caesar_cypher.encode(plaintext_word, best_rotation)
        reconstructed_phrase = reconstructed_phrase.replace(encrypted_word, plaintext_word)
    return reconstructed_phrase
