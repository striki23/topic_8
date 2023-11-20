# Программа находит наименьшее положительное число,
# которое делится на все числа от 1 до n без остатка
# Гарантируется, что 1 < n < 21

n = int(input())

x = n
while x > 0:
    flag = True
    for i in range(1, n+1):
        if x % i == 0:
            continue
        else:
            flag = False
            break
    if flag:
        print(x)
        break
    else:
        x += 1

# очень долго думает при n ~ 21
# возможно нужно начинать перебор ни с n, а с большего числа

