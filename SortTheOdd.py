'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''
def sort_array(array):
    for count in range(2):
        for i in range(len(array)):
            if array[i] % 2 == 1:
                for j in range(len(array)):
                    if array[i] == array[j]: continue
                    elif array[j]%2 == 1:
                        if count == 1 and array[i] > array[j]:
                            array[i], array[j] = array[j], array[i]
                        array[i], array[j] = array[j], array[i]
        
    return array

print(sort_array([5, 3, 2, 8, 1, 4]))
