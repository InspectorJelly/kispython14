import math


def main(x):
    c = 75 * math.cos(x)**6
    c3 = 8*math.cos(93*x**2)**3
    if x < -5:
        return(c3+50*math.ceil(x)**7 + 22*x**4)
    elif -5 <= x < 74:
        return(6*x+28+c*x**2+99*(56-x**2-63*x)**2)
    elif 74 <= x < 128:
        return(88*(x**2-47-85*x)**3+x**4+30*(x**2+x**3/7)**7)
    else:
        return(x/5-85*x**6-0.02)

print(main(131))
print(main(15))
print(main(-2))
print(main(113))
print(main(152))