""" 🔴 ЗАДАНИЕ 5 (сложное)
Есть пустой список numbers.
Программа:
постоянно спрашивает число
если число уже есть в списке — не добавлять
если число новое — добавить
ввод 0 — выход
После выхода:
вывести список
вывести количество уникальных чисел """

numbers = []

while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    elif num not in numbers:
        numbers.append(num)
    else:
        continue
print(numbers)
print(len(numbers))
