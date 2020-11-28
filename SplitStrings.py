'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''

def solution(s):
    result = ''
    result_array = []
    flag = False
    for i in range(len(s)):
        if result == '':
            result += f'{s[i]}'
            flag = True
        elif flag == True:
            result += f'{s[i]}'
            result_array.append(result)
            result = ''
            flag = False
        if i == len(s)-1 and flag == True:
            result_array.append(f'{s[i]}_')

    return result_array
      

print(solution(''))