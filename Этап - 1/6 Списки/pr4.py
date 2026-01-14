""" Пользователь вводит числа.
каждое число добавляется в список
ввод 0 — остановка
после окончания:
выведи список
выведи минимальное и максимальное число """

numbers = []

while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    numbers.append(num)

if numbers:
    print(numbers)
    print(f"Максимальное число: {max(numbers)}")
    print(f"Минимальное число: {min(numbers)}")
else:
    print("Список пуст, вы не ввели ни одного числа")