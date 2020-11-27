def next_happy_year(year):
    a = str(year + 1)  
    while len(set(a)) != len(a):
        a = str(int(a) + 1)
    return int(a)


print(next_happy_year(101010))
