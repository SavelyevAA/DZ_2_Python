from msilib import sequence

n = int(input('Введите число: ')) 

def squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = squerence(n)
print(nums)
print(round(sum(nums), 5))