''' 🧪 ЭКЗАМЕН №2 — УЧЁТ ПОЛЬЗОВАТЕЛЕЙ (УСИЛЕННЫЙ)
📥 Дано (начальные данные)
users = {
    "alex": {"age": 31, "city": "Moscow"},
    "john": {"age": 25, "city": "Berlin"},
    "maria": {"age": 28, "city": "Madrid"}
}
🎯 Задача
Написать программу, которая:
Показывает меню:
1 — Найти пользователя
2 — Добавить пользователя
3 — Обновить данные пользователя
4 — Показать всех пользователей
0 — Выход
Работает в цикле, пока пользователь не выберет 0 '''

users = {
    "alex": {"age": 31, "city": "Moscow"},
    "john": {"age": 25, "city": "Berlin"},
    "maria": {"age": 28, "city": "Madrid"}
}
while True:
    # выводим меню
    menu = input('''Выберите пункт меню:
1 — Найти пользователя
2 — Добавить пользователя
3 — Обновить данные пользователя
4 — Показать всех пользователей
0 — Выход
''')
    # Поиск пользователя в списке
    if menu == "0":
        print(f'Программа завершена')
        break
    elif menu == "1":
        name = input(f'Введите имя: ')  # запросить имя
        name = name.lower()             # сделать все буквы строчными
        if name in users:               # если имя есть в словаре
            print(f'Возраст: {users[name]["age"]}\nгород: {users[name]["city"]}')   # сообщение с возрастом и городом
        else:
            print(f'Пользователь не найден')
    # Добавление Пользователя
    elif menu == "2":
        name = input(f'Введите имя: ')
        name = name.lower() 
        if name in users:
            print(f'Данный пользователь уже существует')
        else:
            while True:
                try:
                    age = int(input(f'Введите возраст: '))
                    city = input(f'Введите город: ')
                    users[name] = {"age" : age, "city" : city}  # добавили данные в словарь
                    print(f'Пользователь добавлен')
                    break
                except ValueError:
                    print("Вы ввели не число")
    # Обновить данные пользователя
    elif menu == "3":
        name = input(f'Введите имя: ')
        name = name.lower() 
        if name not in users:
            print(f'Пользователь не найден')
        else:
            while True:
                try:
                    age = int(input(f'Введите новый возраст: '))
                    city = input(f'Введите новый город: ')
                    users[name] = {"age" : age, "city" : city}
                    print(f'Данные пользователя {name} обновлены')
                    break
                except ValueError:
                    print("Вы ввели не число")
    # Показать всех пользователей
    elif menu == "4":
        for i in users:
            print(f' {i} - {users[i]["age"]} лет, {users[i]["city"]} ')

    
    else:
        print(f'Пункт не найден')