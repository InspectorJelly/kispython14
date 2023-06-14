import math


def main(y):
    x=66*(y**4-y**6)+(((14*(math.cos(y)**3))+(75*(math.log1p(y)**5)))/((9+y**3)**5))
    return(x)

print('%.2e' %main(0.73))
print('%.2e' %main(0.1))
print('%.2e' %main(0.85))
print('%.2e' %main(0.54))
print('%.2e' %main(0.39))