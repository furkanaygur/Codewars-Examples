'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

'''


def pig_it(text):
    result,a = [],''
    for i in text.split():
        a = i[0]
        if i.isalpha():
            result.append(i[1:]+a+'ay')
        else:
            result.append(i)
    return ' '.join(result) 

print(pig_it('Quis custodiet ipsos custodes ?'))