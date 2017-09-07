import math

def quadratic(a, b, c):
    if b*b-4*a*c<0:
        raise TypeError('错误的参数')
    else:
        n1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        n2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return n1,n2

print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
