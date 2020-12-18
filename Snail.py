'''
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


Note 1: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

Note 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''


def snail(snail_map):
    result = []
    def leftToRight(array):
        a = snail_map[0]
        snail_map.remove(snail_map[0])
        return a
        
    def upToBottom(array):
        a = []
        for i in range(len(array)):
            a += array[i][len(array)],
            snail_map[i]= snail_map[i][:-1]
        return a

    def rightToLeft(array):
        a = []
        for i in reversed(array[len(array)-1]):
            a += i,
        snail_map.remove(snail_map[len(array)-1])
        return a

    def bottomToUp(array):
        a = []
        x = len(array)-1
        for i in range(len(array)):
            a += array[x][0],
            snail_map[x]= snail_map[x][1:]
            x -= 1
        return a

    lenght = [len(i) for i in snail_map]

    while True:
        if len(result) != sum(lenght): result += leftToRight(snail_map)
        else: break
        if len(result) != sum(lenght): result += upToBottom(snail_map)
        else: break
        if len(result) != sum(lenght): result += rightToLeft(snail_map)
        else: break
        if len(result) != sum(lenght): result += bottomToUp(snail_map)
        else: break
    
    return result

print(snail([[1,2,3,1], [4,5,6,4], [7,8,9,7],[7,8,9,7]]))