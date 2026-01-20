# ============================
# ЗАГРУЗКА ДАННЫХ ИЗ ФАЙЛА
# ============================

# Открываем файл users.txt в режиме чтения
f = open("users.txt", "r")

# Считываем весь файл в одну строку
file_string = f.read()

# Закрываем файл (обязательно!)
f.close()

# Разбиваем строку по переносам строк
# Получаем список строк вида: ["alex,31,Moscow", "maria,28,Madrid", ...]
file_list = file_string.split("\n")

# Создаём пустой словарь для пользователей
users = {}

# Проходим по каждой строке файла
for i in range(len(file_list)):
    # Если строка пустая — пропускаем её
    if file_list[i] == "":
        continue

    # Берём одну строку
    line = file_list[i]

    # Разбиваем строку по запятой
    # Получаем список: ["alex", "31", "Moscow"]
    parts = line.split(",")

    # Записываем данные в словарь users
    # parts[0] — имя
    # parts[1] — возраст
    # parts[2] — город
    users[parts[0]] = {
        "age": int(parts[1]),
        "city": parts[2]
    }


# ============================
# МЕНЮ (БЕСКОНЕЧНЫЙ ЦИКЛ)
# ============================

while True:
    choice = input(
        "\n1 — Показать всех пользователей\n"
        "2 — Показать пользователей старше N лет\n"
        "3 — Найти пользователя по имени\n"
        "4 — Добавить пользователя\n"
        "0 — Выход\n"
        "Выберите пункт: "
    )

    # ---------- ВЫХОД ----------
    if choice == "0":
        print("Выход из программы.")
        break


    # ---------- 1. ВСЕ ПОЛЬЗОВАТЕЛИ ----------
    elif choice == "1":
        for name in users:
            print(f"{name} — {users[name]['age']} лет, {users[name]['city']}")


    # ---------- 2. ПОЛЬЗОВАТЕЛИ СТАРШЕ N ----------
    elif choice == "2":
        age_limit = int(input("Введите возраст: "))

        names = []

        for name in users:
            if users[name]["age"] >= age_limit:
                names.append(name)

        if len(names) == 0:
            print("Таких пользователей нет.")
        else:
            # Склеиваем имена в строку через запятую
            names_str = ", ".join(names)
            print(f"Пользователи старше {age_limit} лет: {names_str}")
            print(f"Количество: {len(names)}")


    # ---------- 3. ПОИСК ПОЛЬЗОВАТЕЛЯ ----------
    elif choice == "3":
        user_search = input("Введите имя пользователя: ").lower()

        # ВАЖНО: проверка напрямую в словаре
        if user_search in users:
            print(
                f"Имя: {user_search}, "
                f"Возраст: {users[user_search]['age']}, "
                f"Город: {users[user_search]['city']}"
            )
        else:
            print("Пользователь не найден.")


    # ---------- 4. ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ ----------
    elif choice == "4":
        user_name = input("Введите имя нового пользователя: ").lower()

        if user_name in users:
            print("Такой пользователь уже существует.")
        else:
            user_age = int(input("Введите возраст: "))
            user_city = input("Введите город: ")

            # Добавляем в словарь
            users[user_name] = {
                "age": user_age,
                "city": user_city
            }

            # Добавляем в файл
            f = open("users.txt", "a")
            f.write(f"{user_name},{user_age},{user_city}\n")
            f.close()

            print("Пользователь успешно добавлен.")


    # ---------- НЕВЕРНЫЙ ВВОД ----------
    else:
        print("Неверный пункт меню.")
