def my_func(stroka):
    list = stroka.split()
    count = 0
    for el in list:
        if el == "q":
            print("Сумма чисел строки равна: ", sum)
            print("Программа завершена")
        else:
            count = count + int(el)
    return count

stroka = input("Введите строку чисел разделенных пробелом: ")
my_func(stroka)
print("Сумма чисел строки равна: ", my_func(stroka))
sum = int(my_func(stroka))
povtor = input("Хотете продолжить?(yes - да): ")

while povtor == "yes":
    stroka = input("Введите строку чисел разделенных пробелом: ")
    my_func(stroka)
    sum = sum + int(my_func(stroka))
    print("Сумма чисел строки равна: ", sum)
    povtor = input("Хотете продолжить?(yes - да): ")
else:
    print("Программа завершена")
