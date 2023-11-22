numbers = ["21", "85", "150", "190", "135", "515", "80"]

# необходимо перебрать все элементы списка numbers
# и вывести только те числа, которые кратны 5 и меньше 151
# если в списке встречается число более 500, прервать цикл

for number in numbers:
    number = int(number)
    if number > 500:
        break
    if number > 150:
        continue
    elif number % 5 == 0:
        print(number)
