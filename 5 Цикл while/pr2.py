while True:
    password = int(input("Введите пароль: "))
    if password == 1234:
        break
    if not password == 1234:
        print("Введён не верный пароль.")

print("Вы вошли в систему!")
