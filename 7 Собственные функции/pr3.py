""" 🔴 ЗАДАНИЕ 3 (ОЧЕНЬ СЛОЖНОЕ)
Функция с циклом
Создай функцию sum_positive():
внутри функции:
запрашивай числа у пользователя
складывай только положительные
если введено 0 → остановка
функция возвращает сумму
После вызова:
выведи результат
📌 Разрешено:
while
if
return
📌 Запрещено:
глобальные переменные
print внутри функции (кроме ввода) """

def sum_positive():
    summ = 0
    while True:
        number = int(input("Введите число: "))
        if number == 0:
            return summ
        elif number < 0:
            continue
        else:
            summ += number
                            
result = sum_positive()
print(f"Результат: {result}")