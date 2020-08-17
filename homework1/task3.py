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
