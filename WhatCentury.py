'''
Description:
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
'''

def what_century(year):
    result = 0
    if int(year[2:]) != 00:
        result = int(year[:2])+1
    else: result = int(year[:2])
    if result%10 == 1 and result != 11: return str(result)+'st'
    elif result%10 == 2 and result != 12: return str(result)+'nd'
    elif result%10 == 3 and result != 13: return str(result)+'rd'
    else: return str(result)+'th'


print(what_century("2000"))