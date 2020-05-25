from functools import reduce

list1 = [i for i in range(100, 1001, 2)]

def mult(a, b):
    return a * b

print(reduce(mult, list1))
