'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
'''


def square_sum(a):
    total = 0
    sqrt = 0
    for i in a:
        if i == 0:
            total = total + 0
            continue
        if i <= -1:
            i = i * -1
        for x in range(1,i+1):
            sqrt = x*x
        total = total + sqrt
    print(total)
        
square_sum([-5, 0, -14, 20, 7, 2, -14, -12])

 
