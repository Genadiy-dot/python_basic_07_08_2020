"""
второй способ решения задачи
"""
user_num = input("Введите число: ")
user_count = input("Введите разряд числа: ")
if user_num.isdigit():
    n = int(user_num)
    k = int(user_count)
    nn = n * (10 ** k + 1)
    nnn = n * ((10 ** (2 * k)) + 10 ** k + 1)
    sum = n + nn + nnn
    print(sum)

else:
    print("Ошибка ввода") 
