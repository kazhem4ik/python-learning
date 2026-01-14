''' Задание 7 — None как флаг
Создай переменную found = None
Запрашивай числа в цикле
Если пользователь ввёл 7 → found = True
После цикла:
если found is None → "7 не найдено"
иначе → "7 найдено" '''

found = None
while found == None:
    user_input = int(input("Введите число: "))
    if user_input == 7:
        found = True

if found == None:
    print("7 не найдено")
else:
    print("7 найдено")