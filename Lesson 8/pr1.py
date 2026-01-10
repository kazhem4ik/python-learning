""" 🟡 ЗАДАНИЕ 1 — СРЕДНЕЕ
Функция + список + for
ТЗ:
1️⃣ Создай функцию count_even(numbers)
2️⃣ Функция принимает список чисел
3️⃣ Считает количество чётных чисел
4️⃣ Возвращает это количество через return
Разрешено:
for
%
return
Запрещено:
print внутри функции
while """

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


numbers = []

while True:
    num = int(input("Введите число (0 — конец): "))
    if num == 0:
        break
    numbers.append(num)

result = count_even(numbers)
print("Чётных чисел:", result)
