'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
'''
 
def solution(string,markers):
    result = ''  
    for i in string.split('\n'):
        temp, flag = '', False
        for x in i:
            if x in markers: flag = True
            elif x == '\n': flag = False
            elif flag == False: temp += x
        result += temp.rstrip()+'\n'
    return result[:-1]


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))