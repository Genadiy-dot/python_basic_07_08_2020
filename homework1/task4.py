"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции
"""
while True:
    user_num = input("Введите целое число: ")

    if user_num.isdigit():
        user_num = int(user_num)
        break
    else:
        print("Ошибка ввода")
result = 0     # наименьшая из возможных цифра в числе

while user_num and result != 9:
    tmp = user_num % 10      # остаток по модулю 10
    if tmp > result:
        result = tmp   
    user_num //= 10     
print(result)

    


    
        
