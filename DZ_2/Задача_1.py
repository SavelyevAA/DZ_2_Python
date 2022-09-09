num = input("Введите вещественное число: ")
sum = 0
for i in num:
    if i != ".":
        sum = sum + int(i)
print (f"Сумма цифр равна: {sum} ")