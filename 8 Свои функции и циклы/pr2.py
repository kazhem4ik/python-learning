""" 🟠 ЗАДАНИЕ 2 — СЛОЖНОЕ
Фильтрация данных
ТЗ:
1️⃣ Создай функцию positive_numbers(numbers)
2️⃣ На вход — список чисел
3️⃣ Внутри функции:
создать новый список
добавить туда только положительные числа
4️⃣ Вернуть новый список
После вызова:
вывести список
вывести его длину
Разрешено:
for
if
.append()
Запрещено:
input внутри функции
изменение исходного списка """
numbers = [1, 4, -6, 8, -10, 7, 3, 1, -4, -2, 8]
def positive_numbers(numbers):
    result = []
    for i in numbers:
        if i > 0:
            result.append(i)
    return result

spisok = positive_numbers(numbers)
print(spisok)
print(len(spisok))