''' Задание A3 — строки → числа
text = "10 20 30 40"
Сделай список строк
Преврати их в числа
Найди сумму (через for, не sum())
📌 Цель:
тип данных важнее значения '''

''' text = "10 20 30 40"

# 1️⃣ Разбиваем строку на список строк
spisok = text.split()  # ['10', '20', '30', '40']

# 2️⃣ Превращаем строки в числа
int_spisok = []
for i in spisok:
    int_spisok.append(int(i))  # каждое значение превращаем в int

# 3️⃣ Суммируем числа через for
summ = 0
for i in int_spisok:
    summ += i

# 4️⃣ Вывод результата
print(summ)  # 100 '''

text = "10 20 30 40"
summ = 0
for i in text.split():
    summ += int(i)
print(summ)