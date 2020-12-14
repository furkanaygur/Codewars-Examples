'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''

def rot13(message):
    result = ''
    for i in message:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            if ord(i)+13 > 122:
                x = 12 - (122 - ord(i))
                result += chr(97+x)
            elif ord(i)+13 > 90 and ord(i) < 97:
                x = 12 - (90 - ord(i))
                result += chr(65+x)
            else:
                result += chr(ord(i)+13)
        else:
            result += i
    return result
print(rot13("Test"))