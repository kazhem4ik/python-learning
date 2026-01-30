# Строки - Форматирование строк, отладочная печать и сырые строки


# Форматирование строк
print("\nФорматирование строк\n" + "-" * 50)

name = "John"
age = 25

print("My name is " + name + " and I am " + str(age) + " years old")
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")


# Отладочная печать
print("\nОтладочная печать\n" + "-" * 50)

name = "John"
age = 25

print("Имя: ", name)
print("Возраст: ", age)

print(f"{name = }")
print(f"{age = }")


# Сырые строки
print("\nСырые строки\n" + "-" * 50)

print("\n - управляющая последовательность, которая используется для переноса строки")
print(r"\n - управляющая последовательность, которая используется для переноса строки")
print(r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat")