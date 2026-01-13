""" 🔴 ЗАДАНИЕ 3 — ОЧЕНЬ СЛОЖНОЕ
Логика + функции + управление потоком
ТЗ:
1️⃣ Создай функцию analyze_numbers()
2️⃣ Внутри:
бесконечный ввод чисел (while True)
0 — выход из ввода
отрицательные числа игнорируются
3️⃣ Функция должна:
считать сумму положительных
считать их количество
4️⃣ Вернуть два значения:
сумму
количество
После вызова:
вывести сумму
вывести количество
если количество > 0 — вывести среднее значение
Разрешено:
while
if / continue / break
return
Запрещено:
глобальные переменные
print внутри функции """

def analyze_numbers():
    result = []
    number = 0
    summ = 0
    while True:
        inp = int(input("Введите число, для выхода нажмите ""0"": "))
        if inp == 0:
            break
        elif inp < 0:
            continue
        else:
            summ += inp
            number += 1
    result.append(summ)
    result.append(number)
    return result


result = analyze_numbers()

print("Сумма: " + str(result[0]))
print("Кол-во: " + str(result[1]))
if result[1] > 0:
    sred = result[0] / result[1]
    print("Среднее: " + str(sred))
