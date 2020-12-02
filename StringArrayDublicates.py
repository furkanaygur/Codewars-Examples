'''
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

dup(["kelless","keenness"]) = ["keles","kenes"].

Strings will be lowercase only, no spaces. See test cases for more examples.
'''

def dup(array):
    result = []
    for i in array:
        temp = ''
        for j in range(len(i)):
            try:
                if i[j] == i[j+1]: continue
                else: temp += i[j]
            except:temp += i[j]
        result.append(temp)
    return result        

print(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]))