list1 = [int(i) for i in input("Input a list of numbers: ").split()]
new_list = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]
print(new_list)
list_num = [num for num in range(20, 240) if num % 20 == 0 or num % 21 == 0]
print(list_num)
