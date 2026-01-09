""" 🔴 ЗАДАНИЕ 3 (ТЯЖЁЛОЕ)
Генерация + логика
1️⃣ Сгенерируй список чисел от 1 до 50
2️⃣ С помощью for:
если число делится на 3 → добавить в список three
если делится на 5 → добавить в список five
если делится на 3 и 5 → добавить в список three_five
3️⃣ В конце вывести:
все три списка
количество элементов в каждом """
three = []
five = []
three_five = []
numbers = list(range(1, 51))
for i in numbers:
    if i % 3 == 0:
        three.append(i)
    if i % 5 == 0:
        five.append(i)
    if i % 3 == 0 and i % 5 == 0:
        three_five.append(i)
    else:
        continue
print(three)
print(five)
print(three_five)