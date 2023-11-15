# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
number = int(input())
if number < 1:
    print('Введите число от 1 и больше')
else:
    sum = 0
    for x in range(1, number + 1):
        sum += x
        if sum >= 100:
            print(f'Сумма всех чисел в диапазоне от 1 до {number} больше 100')
            break
        else:
            continue
    print(sum)
# Недоработала! выводит лишнюю сумму.....
