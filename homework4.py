def my_func(x, y):
    if y == 0:
        return 1
    result = x * my_func(x, y-1)
    return result
a = int(input("Введите число для возведения в степень: "))
b = int(input("Введите степень: "))
print(my_func(a, b))
