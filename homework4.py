str1 = input("Write a few words: ")
list1 = str1.split()
for i, word in enumerate(list1, 1):
    print(f"{i} {word[:10]}")
