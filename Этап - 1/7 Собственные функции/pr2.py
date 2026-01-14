""" 🟠 ЗАДАНИЕ 2 (СЛОЖНОЕ)
Функция калькулятора
Создай функцию calculate(a, b, operation), которая:
принимает:
два числа
строку с операцией ("+", "-", "*", "/")
возвращает результат
если операция неизвестна → вернуть строку "Ошибка"
📌 Требования:
деление на 0 обработать
print только при вызове функции, не внутри """

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operation = (input("Введите операцию: "))

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "На 0 делить нельзя"
        else:
            return a / b
    else:
        return "Ошибка"
    
result = calculate(a, b, operation)
print(f"Результат: {result}")