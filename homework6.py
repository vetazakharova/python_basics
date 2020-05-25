def factorial(n):
    if n == 1:
        yield 1
        return 1
    else:
        generator = list(factorial(n-1))
        x = n * generator[0]
        yield x
        return x

print(list(factorial(int(input("What factorial do you want to calculate: ")))))
