# Программа находит наименьшее положительное число,
# которое делится на все числа от 1 до n без остатка
# Гарантируется, что 1 < n < 21

from math import factorial

n = int(input())

prod = factorial(n)

x = n
while x < prod:
    for i in range(1, n + 1):
        if x % i != 0:
            break
    else:
        print(x)
        break
    x += n
