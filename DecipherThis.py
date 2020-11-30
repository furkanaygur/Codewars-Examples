'''
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'

'''

def decipher_this(string):
    result  = '' 
    for i in string.split(' '):
        number, chars  = '', []
        for j in i:
            if j.isnumeric(): number += str(j)
            else: chars += j,
        result += chr(int(number))
        if len(chars) >= 2: chars[0], chars[-1] = chars[-1], chars[0] 
        result += ''.join(chars) + ' '
    return result.rstrip()   
    
print(decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka'))