''' Задача 3 — экзамен
Есть список:
numbers = list(range(1, 21))  # [1, 2, 3, ..., 20]
Нужно:
Получить список квадратов каждого третьего числа.
Составить список чисел, которые идут через одно, но только из второй половины исходного списка.
Реверсировать список и оставить только те числа, которые делятся на 4. '''

numbers = list(range(1, 21))
num1 = numbers[::3]
quat = []
for i in num1:
    i **= 2
    quat.append(i)

num2 = numbers[10::2]

num3 = numbers[::-1]
delen = []
for i in num3:
    if i % 4 != 0:
        continue
    delen.append(i)

print(quat)
print(num2)
print(delen)