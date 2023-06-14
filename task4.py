import math


def f(n):
    if (n == 0):
        return (-0.72)
    elif (n == 1):
        return (0.31)
    elif (n >= 2):
        return(63 - f(n-1) - math.fabs(f(n-2))**2)

print(f(7))
print(f(5))
print(f(8))
print(f(9))
print(f(6))