def my_func(var_1, var_2, var_3):
    x = var_1
    y = var_2
    z = var_3
    max_1 = z
    max_2 = z
    if x > y:
        max_1 = x
        if z > x:
            max_2 = z
        else:
            max_2 = y
    elif y > x:
        max_1 = y
        if x > z:
            max_2 = x
        else:
             max_2 = z
    elif y == x:
        max_1 = y
        if x > z:
            max_2 = x
        else:
             max_2 = z
    return max_1 + max_2

var_1 = int(input("Введите 1 число: "))
var_2 = int(input("Введите 2 число: "))
var_3 = int(input("Введите 3 число: "))

my_func(var_1, var_2, var_3)
print(my_func(var_1, var_2, var_3))