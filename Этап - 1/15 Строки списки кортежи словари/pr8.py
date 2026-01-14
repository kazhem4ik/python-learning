# 1️⃣ Создаём словарь с пользователями
users = {
    "Андрей" : {"age" : 31, "status" : "Работает", "format" : "Удаленно"},
    "Алексей" : {"age" : 25, "status" : "Работает", "format" : "Удаленно"},
    "Николай" : {"age" : 27, "status" : "Работает", "format" : "Офис"},
    "Владимир" : {"age" : 30, "status" : "Работает", "format" : "Удаленно"},
    "Антон" : {"age" : 23, "status" : "Работает", "format" : "Офис"}
}
def add_users():
    while True:
        name_input = input("Введите имя пользователя или нажмите 0 для выхода: ")
        if name_input == "0": break
        age_input = input("Введите возраст пользователя: ")
        status_input = input("Введите статус пользователя: ")
        format_input = input("Введите формат работы пользователя: ")
        users[name_input] = {"age" : str(age_input), "status" : status_input, "format" : format_input}
        print(f"Пользователь {name_input} добавлен!")
    return users

while True:
    user_input = input("Вы хотите добавить нового пользователя? ")
    if user_input == "Да": add_users()
    elif user_input == "Нет": break
    else: print(f'Введите "Да" или "Нет')
print(users)
# 4️⃣ Выводим итоговый словарь
#name = input("Введите имя пользователя: ")
#print(f"Сотрудник {name.title()}\nвозраст: {users[name.title()]['Возраст']} год\nстатус: {users[name.title()]['Статус']}\nформат работы: {users[name.title()]['Формат']}")

