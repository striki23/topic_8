# Программа запрашивает у пользователя целое число
# и проверяет, является ли оно простым

number = int(input('Введите число: '))

if number <= 0:
    print('Число должно быть положительным')
else:
    for x in range(2, number+1):
        if number % x == 0 and number / x != 1:
            print(f'Число {number} не является простым')
            break
        elif number % x != 0:
            continue
        else:
            print(f'Число {number} является простым')