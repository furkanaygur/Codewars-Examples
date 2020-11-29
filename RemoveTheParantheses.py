'''
Remove the parentheses
In this kata you are given a string for example:

"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"
Notes
Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like "[]" and "{}" as these will never appear.
There can be multiple parentheses.
The parentheses can be nested.

'''

def remove_parentheses(s):
    result = ''
    a = 0
    start = 0
    for i in range(len(s)):
        if s[i] == '(':
            a += 1
            continue
        elif s[i] == ')':
            if a == 0: continue
            a -=1
            if a >= 1: start = i+1
            continue
        if a == 0: result += s[i]
    if a >= 1: result += s[start:]
    if result == '': return '  '
    return result
            


    
 

print(remove_parentheses('sBtJXYI()DpVxQWId MWVozwWva kri obRgP AXjTKQUjXj xoEA xmkTQ LvrfGyNzCTqHHTWFPuLvrRWba fnWbFNVQBANn ZqwHzLTxkSuAPQiccORuQHNLxlaiYJSTESsOMoMooVbvDxZiEbilrgJeUfACIeEw AzPXkOrDk vjAAaqiPyMIOl  UvLWq UMigMOi YRwiiOFcNRVyZbAPajY e YHldtivKMbFGwr pfKGlBRBjq wiHlobnqR GNMxf eW veFKMNzopYXf sG)VAyjLrHjxwNR ZPlkAp NRyKEKCM'))
