def too_chisla (x, y):
    if int(y) == 0:
        return ("Делить на ноль нельзя")
    else:
        z = x / y
        return x / y

x = float(input("Введите первое число: "))
y = float(input("Введите первое число: "))

print(too_chisla(x, y))
