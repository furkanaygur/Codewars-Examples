'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

import string
def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    for i in s.lower():
        if i in alphabet:
            alphabet.remove(i)   
    if len(alphabet) == 0: return True
    return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))