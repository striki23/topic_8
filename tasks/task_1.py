data_types = [
    1852, 12.43, True, 4 + 3j, "Bravo!",
    (13, -5), 3.5e10, 100.95, "abcdef",
    [21, 49], {"name": 'Micky', "age": 17}
]

# Программа, которая выводит каждый элемент и тип данных из data_types
# Исключение тип float или str
for x in data_types:
    if type(x) in (float, str):
        continue
    print('Элемент:', x, 'Тип:', type(x))

# Option 2
for x in data_types:
    typeof = type(x)
    if typeof not in (float, str):
        print('Элемент:', x, 'Тип:', typeof)

# Option 3
for x in data_types:
    if not isinstance(x, (float, str)):
        print('Элемент:', x, 'Тип:', type(x))
