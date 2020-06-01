with open("file3.txt", "r") as file3:
    salary = []
    below = []
    my_list = file3.read().split('\n')
    for i in my_list:
        a = i.split()
        if int(a[2]) < 20000:
            below.append(a[0])
        salary.append(a[2])
    print(f"Those workers earn less then 20000: {below}, and the average salary is {sum(map(int, salary)) / len(salary)}" )
