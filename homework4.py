numbers = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
file4_new = []
with open("file4.txt", "r") as file4:
    #content = file4.read().split("\n")
    for i in file4:
        i = i.split()
        file4_new.append(numbers[i[0]] + "-" + i[2] + "\n")
    print(file4_new)
with open("file4_new.txt", "w") as file4new:
    file4new.writelines(file4_new)
