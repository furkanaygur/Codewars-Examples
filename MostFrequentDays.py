'''
What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Preconditions:

Week starts on Monday.
Year is between 1583 and 4000.
Calendar is Gregorian.
Example:

most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']
'''


import datetime
def most_frequent_days(year):
    days = {'Monday':0,
            'Tuesday':0,
            'Wednesday':0,
            'Thursday':0,
            'Friday':0,
            'Saturday':0,
            'Sunday':0
    }
    result = []
    for month in range(1,13):
        for day in range(1,32):
            try:
                x = datetime.datetime(year,month,day)
                day = x.strftime("%A")
                days[day] = days[day]+1
            except: pass
    
    d = max(days, key = lambda k: days[k])
    result.append(d)
    value = days[d]
    del days[d]
    c = max(days, key = lambda k: days[k])
    if value == days[c]: result.append(c)
    return result        

print(most_frequent_days(2020))