def division(arg1, arg2):
    if arg2 == 0:
        print("Can't divide by zero!")
    else:
        result = int(arg1 / arg2)
        return result
num1 = int(input("Input the divided number: "))
num2 = int(input("Input the dividing number: "))
print(division(num1, num2))
