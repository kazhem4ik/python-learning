''' 📁 Проект: «User Analyzer» (консольное приложение)
🎯 Цель
Закрепить:
строки
split
списки
словари
range / len
файлы
логику обработки данных
Без классов. Без JSON. Только чистый Python. '''

# 1. Открывает файл, считывает весь файл, разбивает его на строки, преобразует данные в словарь
f = open("users.txt", "r")
file = f.read()
file_parts = file.split("\n")
f.close()
users = {}
for i in range(len(file_parts)):
    parts = file_parts[i]
    drob = parts.split(",")
    users[drob[0]] = {"age" : drob[1], "city" : drob[2]}

# 2. Вывести всех пользователей старше 25 лет, Вывести их имена одной строкой, через запятую (без запятой в конце!),Вывести количество таких пользователей
# Делаем список из пользователей старше 25 лет
olds_list = []
for name in users:
    if int(users[name]["age"]) >= 25:
        olds_list.append(name)
        
# Делаем из этого списка строку с запятыми
olds = ""
for i in range(len(olds_list)):
    olds += olds_list[i]
    # Ставим запятую, если i не равно длине списка - 1 (длина списка 3 - 1 = 2)
    if i != len(olds_list) - 1:
        olds += ", "
        
print(f"Пользователи старше 25 лет: {olds}")
print(f"Всего пользователей старше 25 лет: {len(olds_list)}")

# Поиск пользователя: Запросить имя через input, Привести ввод к нижнему регистру, Если пользователь есть: Имя: maria Возраст: 28 Город: Madrid, Если нет — корректное сообщение

user = input(f"Введите имя пользователя: ")
user_name = user.lower()
if user_name in users:
    print(f'Имя: {user_name}, Возраст: {users[user_name]["age"]}, Город: {users[user_name]["city"]}')
else:
    print(f'Данного пользователя нет в списке.')