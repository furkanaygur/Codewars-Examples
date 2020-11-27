import math
def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    if math.sqrt(n) % 1 == 0:
        return True
    return False
     
print(is_square(25))