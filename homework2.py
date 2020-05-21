list1 = []
val1 = input("введите ряд любых чисел: ")
list1 = val1.split()

for i in range(1, len(list1), 2):
    list1[i], list1[i-1] = list1[i-1], list1[i]
    
print(list1)
