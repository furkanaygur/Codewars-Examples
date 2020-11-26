'''
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

8kyu
'''

def sentenceSmash(array):
    return ' '.join(array)

print(sentenceSmash(['furkan','aygur']))


'''
Calculate the total score (sum of the individual character scores) of a sentence given the following score rules for each allowed group of characters:

Lower case [a-z]: 'a'=1, 'b'=2, 'c'=3, ..., 'z'=26
Upper case [A-Z]: 'A'=2, 'B'=4, 'C'=6, ..., 'Z'=52
Digits [0-9] their numeric value: '0'=0, '1'=1, '2'=2, ..., '9'=9
Other characters: 0 value
Note: input will always be a string

'''

def senteceCalculator(sentence):
    total = 0
    for i in sentence:
        if i.isnumeric():
            total += int(i)
            print(i)
        elif i != ' ' and (int(ord(i))>= 97 and int(ord(i))<=122):
            total += int(ord(i)-96)
            print(i,ord(i)-96)
        elif i != ' ' and (int(ord(i))>= 65 and int(ord(i))<=90):
            total += int(ord(i)-64) *2
            print(i,int(ord(i)-64) *2)
    return total

print(senteceCalculator('oops, i did it again!'))