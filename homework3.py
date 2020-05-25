list1 = [int(i) for i in input("Input a list of numbers: ").split()]
new_list = [i for i in list1 if list1.count(i) == 1]
print(new_list)
