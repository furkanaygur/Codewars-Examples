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
    for i in s:
        if i == '(': a += 1
        elif i == ')': a -=1
        elif a == 0: result += i
    return result
            


    
 

print(remove_parentheses('sBtJXYI()DpVxQWId MWVozwWva kri obRgP AXjTKQUjXj xoEA xmkTQ LvrfGyNzCTqHHTWFPuLvrRWba fnWbFNVQBANn ZqwHzLTxkSuAPQiccORuQHNLxlaiYJSTESsOMoMooVbvDxZiEbilrgJeUfACIeEw AzPXkOrDk vjAAaqiPyMIOl  UvLWq UMigMOi YRwiiOFcNRVyZbAPajY e YHldtivKMbFGwr pfKGlBRBjq wiHlobnqR GNMxf eW veFKMNzopYXf sG)VAyjLrHjxwNR ZPlkAp NRyKEKCM'))
