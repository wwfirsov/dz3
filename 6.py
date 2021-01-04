def int_func(stroka):
    result = stroka.title()

    return result

stroka = input("Введите слово из маленьких латинских букв: ")
int_func(stroka)
print("Результат: ", int_func(stroka))