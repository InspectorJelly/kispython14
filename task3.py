import math


def main(b, n, m):
    sum = 1
    for i in range(1, m+1):
        sum1 = 0
        for k in range(1, n+1):
            sum2 = 0
            for c in range(1, b+1):
                sum2 += 70 * (math.floor(i / 76 + c ** 3 / 95 + 81)) ** 5 \
                        + 50 * k ** 2
            sum1 += sum2
        sum *= sum1
    return (sum)

print(main(8, 6, 3))
print(main(8, 4, 2))
print(main(8, 2, 5))
print(main(5, 5, 8))
print(main(8, 5, 8))