# Программа выводит на экран все простые числа в заданном диапазоне

start_number = int(input('Введите начало диапазона:'))
end_number = int(input('Введите конец диапазона:'))

# если начало и конец диапозона равны или
# являются отрицательными значениями выводим сообщение об ошибке
if (start_number == end_number
        or start_number < 0
        or end_number < 0):
    print('Некорректный диапазон')

# Если начало диапазона больше конца меняем порядок
elif start_number > end_number:
    start_number, end_number = end_number, start_number

# в ином случае ищем простые числа в диапозоне
else:
    print('Простые числа в заданном диапазоне:', end=' ')
    for i in range(start_number, end_number + 1):
        for j in range(2, i + 1):
            if i % j == 0 and i / j != 1:
                break
            elif i % j != 0:
                continue
            else:
                print(i, end=' ')
