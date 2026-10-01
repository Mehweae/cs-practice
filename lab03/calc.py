x = int(input("Введите первое число:"))
y = int(input("Введите второе число:"))
sign = input("Введите знак действия (+, -, / или *):")
if sign == "+":
    print(x+y)
elif sign == "-":
    print(x-y)
elif sign == "*":
    print(x*y)
elif sign == "/":
    print(x/y)
else:
    print("Ошибка ввода знака")