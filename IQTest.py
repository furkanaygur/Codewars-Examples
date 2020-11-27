'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
'''

def iq_test(numbers):
    numbers = numbers.split()
    my_list = []
    
    for i in numbers:
        if int(i) %2 == 0:
            my_list.append(True)
        else:
            my_list.append(False)
        
    temp = my_list[0]
    for i in range(1,len(my_list)):
        if temp != my_list[i]:
            try:
                if temp == my_list[i+1]:
                    return i+1
                return i
            except:
                return i+1
             

print(iq_test('14 24 24 26 10 40 8 40 42 0 0 50 42 18 16 1'))