'''
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
'''

def pyramid(n):
    result = []
    for i in range(1,n+1):
        temp = []
        for j in range(i): temp.append(1)
        result.append(temp)
    return result


print(pyramid(4))