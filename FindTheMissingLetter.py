'''
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)


'''

def find_missing_letter(chars):
    missing_letters = ''
    for i in range(len(chars)):
        try:
            a = ord(chars[i+1]) - ord(chars[i])
            if a != 1:
                chars.insert(i+1,chr(ord(chars[i])+1))
                missing_letters = missing_letters + ', ' + chr(ord(chars[i])+1)
        except:
            pass
    return chars,f' Missing Letters: {missing_letters}'

print(find_missing_letter(['O','Q','S']))
