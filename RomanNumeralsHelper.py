'''
Task
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
| Symbol | Value |
|----------------|
| I      |  1    |
| V      |  5    |
| X      |  10   |
| L      |  50   |
| C      |  100  |
| D      |  500  |
| M      |  1000 |
'''

class RomanNumerals():
    def to_roman(self,num):
        romans = {1:'I', 5:'V', 10:'X',  50:'L',  100:'C', 500:'D', 1000:'M'}
        result = []
        if num in romans: return romans[num]
        else:
            x = ['1']
            [x.append('0') for i in range(len(str(num))-1)]
            x = int(''.join(x))
            for i in range(len(str(num))):
                if 1 <= num//x <=3: [result.append(romans[1*x]) for i in range(num//x)]
                elif num//x == 4:
                    result.append(romans[1*x])
                    result.append(romans[5*x])
                elif num//x == 5:  result.append(romans[5*x])
                elif 6<= num//x <=8:
                    result.append(romans[5*x])
                    [result.append(romans[x]) for i in range(num//x - 5)]
                elif num//x == 9:
                    result.append(romans[1*x])
                    result.append(romans[1*x*10])
                if  x != 1:
                    num = num - num//x*x
                    print(num,x)
                    x = int(str(x)[:-1])
            return ''.join(result)

r1 = RomanNumerals()
print(r1.to_roman(2020))
