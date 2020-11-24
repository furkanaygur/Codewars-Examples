'''
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []

'''

def invertValues(array=''):
    if array == '':
        return array
    for i in range(len(array)):
        array[i] = array[i] *  -1
    return array


print(invertValues([]))