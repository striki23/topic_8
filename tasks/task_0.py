# программа, которая считывает целые числа с клавиатуры до тех пор,
# пока не будет введено три отрицательных числа

count = 0
summ_positive = 0
summ_negative = 0

while True:
    if count == 3:
        break
    else:
        number = int(input())
        if number <= 0:
            count += 1
            summ_negative += number
        else:
            summ_positive += number

print('Сумма положительных чисел:', summ_positive)
print('Сумма отрицательных чисел:', summ_negative)
