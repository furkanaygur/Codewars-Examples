'''
Description:
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
'''

def parse_int(string):
    n = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
        'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19 }
    ns = {'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90 }
    th = {'hundred':100, 'thousand':1000, 'million':1000000 } 
    result = 0
    flag = False
    temp = 0
    for i in string.split():
        for j in i.split('-'):
            print(result)
            if j in n:
                result += n[j]
            elif j in ns:
                result += ns[j]
            elif j in th:
                if j == 'thousand' and flag == False:
                    result *= th[j]
                    flag = True
                else:
                    flag = False
                    temp = str(result)[-1]
                    result -= int(temp)
                    temp = int(temp) * th[j]
                    result += int(temp)
    return result

print(parse_int('seven hundred thousand'))