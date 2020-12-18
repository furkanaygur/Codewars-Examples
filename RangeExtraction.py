'''
Description:
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''

def solution(args):
    temp = []
    result = []
    for i in range(len(args)):
        try:
            if args[i+1] - args[i] == 1: temp += args[i],
            else:
                if temp != [] and len(temp) > 2:
                    temp += args[i],
                    result.append(str(temp[0])+'-'+str(temp[-1])+',')
                    temp = []
                elif 0 < len(temp) <= 2:
                    temp += args[i],
                    if len(temp) > 2: result.append(str(temp[0])+'-'+str(temp[-1])+',')
                    else: [result.append(str(i)+',') for i in temp]
                    temp = []
                else: result.append(str(args[i])+',')
        except:
            if temp != []:
                temp += args[i],
                result.append(str(temp[0])+'-'+str(temp[-1]))
            else: result.append(str(args[i]))
            
    return ''.join(result).lstrip(',')
     

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))

