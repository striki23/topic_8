# Программа вычисляет сумму всех чисел от 1 до n (n вводит пользователь).
# Если сумма чисел менее 100, то она выводится в консоль,
# в противном случае выводится сообщение
number = int(input())
flag_100 = False
if number < 1:
    print('Введите число от 1 и больше')
else:
    summ = 0
    for x in range(1, number + 1):
        summ += x
        if summ >= 100:
            print(f'Сумма всех чисел в диапазоне от 1 до {number} больше 100')
            flag_100 = True
            break
        else:
            continue
    if not flag_100:
        print(summ)
