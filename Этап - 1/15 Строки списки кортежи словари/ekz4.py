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
file1 = f.read()    # - file1 = "alex,31,Moscow\njohn,25,Berlin\nmaria,28,Madrid\nkate,19,London"
lines = file1.split("\n")   # - lines = "['alex,31,Moscow', 'john,25,Berlin', 'maria,28,Madrid', 'kate,19,London']"
parts = []
for i in range(len(lines)):
    part = lines[i].split(",")
    parts += part
    
print(parts)