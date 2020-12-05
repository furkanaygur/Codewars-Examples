'''
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''


def encrypt_this(text):
    if text == '': return text
    result= '' 
    for i in text.split(' '):
        chars = []
        result += ' '+str(ord(i[0]))
        for j in range(1,len(i)):
            chars += i[j],
        if len(chars) >= 2: chars[0], chars[-1] = chars[-1], chars[0]
        result += ''.join(chars)
    return result.lstrip()


print(encrypt_this('A wise old owl lived in an oak'))