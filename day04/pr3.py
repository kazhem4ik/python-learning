num1 = int(input("Введите первое число: "))
symbol1 = input("Введите операцию (+, -, /, *): ")
num2 = int(input("Введите второе число: "))

if symbol1 == "+":
    print(num1 + num2)
elif symbol1 == "-":
    print(num1 - num2)
elif symbol1 == "/":
    if num2 == 0:
        print("На 0 делить нельзя!")
    else:    
        print(num1 / num2)
elif symbol1 == "*":
    print(num1 * num2)
else:
    print("Неизвестная операция")
