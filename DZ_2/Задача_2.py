factorial = int (input("Введите число: "))
product = 1
for i in range (1,factorial + 1) :
    product *= i
    print (product ,end = "  " )