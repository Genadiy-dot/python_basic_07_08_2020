"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
user_num = input("Введите число: ")
if user_num.isdigit():
    n = int(user_num)
    nn = int(f"{n}{n}")
    nnn = int(f"{n}{n}{n}")
    sum = n + nn + nnn
    print(sum)
else:
    print("Ошибка ввода")    
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



