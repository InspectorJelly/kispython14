from math import ceil, exp


def main(y):
    r = 0
    n = len(y) - 1
    for i in range(1, len(y) + 1):
        r += 20 * exp(y[n + 1 - i]** 2 / 36 + y[n + 1 - ceil(i / 2)]) ** 2
    return r

y = [0.36, -0.54, 0.03, 0.61, -0.72, 0.9]
print(main(y))
#print(main([0.81, 0.23, -0.44, -0.07, 0.52, -0.06]))
#print(main([0.36, -0.54, 0.03, 0.61, -0.72, 0.9]))
#print(main([-0.51, -0.09, 0.55, -0.87, 0.45, -0.12]))
#print(main([0.3, 0.06, -0.18, 0.03, -0.66, 0.58]))
#print(main([-0.48, -0.69, -0.08, -0.68, -0.01, -0.79]))