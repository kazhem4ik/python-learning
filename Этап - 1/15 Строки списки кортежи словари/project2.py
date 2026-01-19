# Написать код, который: Открывает файл, Считывает данные, Превращает их в словарь:
f = open("users.txt", "r")
file_string = f.read()
file_list = file_string.split("\n")
f.close()
users = {}
for i in range(len(file_list)):
    parts = file_list[i]
    parts_list = parts.split(",")
    users[parts_list[0]] = {"age" : int(parts_list[1]), "city" : parts_list[2]}
    
# Сделать бесконечный цикл с меню:
# 1 — Показать всех пользователей,
# 2 — Показать пользователей старше N лет, 
# 3 — Найти пользователя по имени,
# 4 — Добавить пользователя, 
# 0 — Выход

while True:
    user_input = input('''1 — Показать всех пользователей
2 — Показать пользователей старше N лет
3 — Найти пользователя по имени
4 — Добавить пользователя
0 — Выход
Выберите пункт 0 - 4: ''')
    if user_input == '0':
        break
    elif user_input == '1':
        for i in users:
            print(f'{i} - {users[i]["age"]} лет, {users[i]["city"]}')
    elif user_input == '2':
        user_age = int(input(f'Введите возраст: '))
        names = []
        for name in users:
            if users[name]["age"] >= user_age:
                names.append(name)
        #print(names)
        names_str = ""
        count = 0
        for i in range(len(names)):
            names_str += names[i]
            count += 1
            if i != int(len(names)) - 1:
                names_str += ", "
    elif user_input == '3':
        user_search = input(f'Введите имя пользователя: ')
        user_search.lower()
        for name in users:
            if user_search == name:
                print(f'Пользователь {user_search} - возраст: {users[name]["age"]}, город {users[user_search]["city"]}')
                
