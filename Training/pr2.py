''' 🟡 ЗАДАНИЕ 2 — СРЕДНЕЕ
Функция + список + None
Нужно:
создать функцию
на вход она получает список чисел
внутри:
если список пустой → вернуть None
иначе → вернуть среднее арифметическое
После вызова:
если функция вернула None → вывести сообщение
иначе → вывести результат
🔒 Разрешено:
for
if
return
🔒 Запрещено:
input внутри функции
try/except '''


spisok = []
# Создал функцию
def sred(numbers):
    # если numbers пустой (False)
    if not numbers:
        return None
    
    summ = 0
    quanity = 0
    # цискл for проходит по списку, считает сумму внутри списка, считает сколько всего чисел
    for i in numbers:
        summ += i
        quanity += 1
    # вовзращаем итог деления суммы на количество чисел
    return summ / quanity    

result = sred(spisok)
if result is None:
    print("Список пуст")
else:
    print("Среднее:", result)
