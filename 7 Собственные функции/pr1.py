""" 🟡 ЗАДАНИЕ 1 (СРЕДНЕЕ)
Функция проверки числа
Создай функцию is_even(number), которая:
принимает одно число
возвращает:
True, если число чётное
False, если нечётное
После этого:
вызови функцию несколько раз
выведи результат через print
📌 Разрешено:
def
if / else
return
📌 Запрещено:
print внутри функции """

number = int(input("Введите число: "))
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(number))