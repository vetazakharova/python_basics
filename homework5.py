list1 = [8, 7, 6, 6, 3, 3, 1]
number = int(input("Input a new number into the rating: "))
n = 0
for i in list1:
    if number <= i:
        n = n + 1
list1.insert(n, number)
print(list1)
