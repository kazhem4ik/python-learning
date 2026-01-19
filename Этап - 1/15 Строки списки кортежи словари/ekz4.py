''' 🧪 Задание — “Пользователи из файла”
📂 Дано (файл users.txt)
alex,31,Moscow
john,25,Berlin
maria,28,Madrid
kate,19,London
Формат: имя,возраст,город
Каждый пользователь в новой строке
🎯 Задача
Прочитать файл users.txt построчно
Преобразовать каждую строку в словарь вида:
{"alex": {"age": 31, "city": "Moscow"}}
Сохранить все данные в один словарь users
Вывести:
список всех пользователей
возраст Maria
город Kate
🔹 Ограничения
❌ без функций
❌ без JSON
❌ без with open(..., encoding="...") (пока просто open)
✅ использовать .split(",")
✅ использовать циклы и словари '''

f = open("users.txt", "r")
file1 = f.read()    # - file1 - это СТРОКА: "alex,31,Moscow\njohn,25,Berlin\nmaria,28,Madrid\nkate,19,London"
lines = file1.split("\n")   # - lines - стал СПИСКОМ, который получился из строки = ['alex,31,Moscow', 'john,25,Berlin', 'maria,28,Madrid', 'kate,19,London']
f.close()
users = {}
for i in range(len(lines)):     # - range(len(lines)) = 0, 1, 2, 3
    line = lines[i]             # - переменная line принимает в себя значения,  СТРОКИ: 'alex,31,Moscow', далее на следующем шаге цикла john,25,Berlin .....
    parts = line.split(",")     # - преобразуем СТРОКУ в СПИСОК на каждом этапе цикла ['alex', '31', 'Moscow'], далее ['john', '25', 'Berlin']
    users[parts[0]] = {"age" : int(parts[1]), "city" : parts[2]}    # - записываем данные в СЛОВАРЬ users
    
print('Все пользователи:', users)
print(f'Возраст Maria: {users["maria"]["age"]}')
print(f'Город Kate: {users["kate"]["city"]}')