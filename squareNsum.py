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

 