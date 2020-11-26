'''
Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

tripleX("abraxxxas") → true
tripleX("xoxotrololololololoxxx") → false
tripleX("softX kitty, warm kitty, xxxxx") → true
tripleX("softx kitty, warm kitty, xxxxx") → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false

7kyu
'''

def triple_x(s):
    firstX = False
    xCounter = 0
    for i in s:
        if i == 'x':
            if not firstX:
                firstX = True
                xCounter += 1
            elif firstX:
                xCounter += 1
        else:
            if xCounter >= 1:
                break

    if xCounter>2:
        return True
    return False

print(triple_x('xxXx'))