# Vocabulary
#
# Description: Identifies all unique words in a text file.
#
# Input
#  source: path to a text file
#
# Output
#
#   unique_words: set of unique words in text
# 

import re

def load(source):
    corpus = open(source, "r", errors='ignore').read().lower()

    regex = "[a-z]+(?:(?:'|-)[a-z]+)?(?:(?:'|-)[a-z]+)?"
    words = re.findall(regex, corpus)
    unique_words = set(words)

    return unique_words
