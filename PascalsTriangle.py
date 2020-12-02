'''
In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula (n k) = n!/(n-k)!, where n denotes a row of the triangle, and k is a position of a term in the row.

Task
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.

n guarantees that terms of the Triangle won't overflow.

Example:
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]

RESULT :

***********************[1]************************
**********************[1, 1]**********************
********************[1, 2, 1]*********************
*******************[1, 3, 3, 1]*******************
*****************[1, 4, 6, 4, 1]******************


'''

def pascals_triangle(n):
    a, temp, temp2 = [1], [1], [1]
    space = 50
    print(f'{temp}'.center(50,'*'))
    for i in range(1,n):
        for j in range(len(temp)):
            try:temp2.insert(j+1,temp[j] + temp[j+1])
            except: temp2.append(1)
        temp = temp2
        print(f'{temp2}'.center(space,'*'))
        for d in temp2: a.append(d)
        temp2 = [1]

    return a

print(pascals_triangle(5))



# *************************************************************************************

# this version return a nested array

def pascal(n):
    a, temp, temp2 = [[1]], [1], [1]
    for i in range(1,n):
        for j in range(len(temp)):
            try:temp2.insert(j+1,temp[j] + temp[j+1])
            except: temp2.append(1)
        temp = temp2
        a.append(temp2)
        temp2 = [1]

    return a

