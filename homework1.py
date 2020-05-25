from sys import argv

name, hours, rate, bonus = argv

def func_salary(hour, rat, bon):
    salary = int(hour) * int(rat) + int(bon)
    return salary

print("Your salary is " + str(func_salary(hours, rate, bonus)))
