'''
Description:

Input
Range is 0-999

There may be duplicates

The array may be empty

Example
Input: 1, 2, 3, 4
Equivalent names: "one", "two", "three", "four"
Sorted by name: "four", "one", "three", "two"
Output: 4, 1, 3, 2
Notes
Don't pack words together:
e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"
'''

def sort_by_name(arr):
    n = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',100:'hundred', 
        1000:'thousand'}
    
    temp = []
    result = []
    t = ''

    for i in arr:
        if i not in n:
            if len(str(i)) == 2:
                t = str(n[i//10 * 10]) + ' '
                t += str(n[i%10])
                temp.append(t)
            if len(str(i)) == 3:
                t = str(n[i//100]) + ' hundred '
                if int(i%100) != 0 and i%100 in n:
                    t += str(n[i%100])
                else:
                    i = i%100
                    if i != 0:
                        t += str(n[i//10 * 10]) + ' '
                        t += str(n[i%10])
                temp.append(t)
        else:
            temp.append(n[i])
    for i in sorted(temp):
        c = temp.index(i)
        result.append(arr[c])

    return result

print(sort_by_name([300, 238, 231]))