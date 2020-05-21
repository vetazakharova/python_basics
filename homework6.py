list1 = []
dist1 = {"name" : "", "price" : "", "quantity" : "", "measurment" : ""}
dict2 = {"name" : [], "price" : [], "quantity" : [], "measurment" : []}
num = 0

while True:
    if input("For exiting the program press 'Q': ").upper() == "Q":
        break
    num = num + 1
    for i in dict1.keys():
        _ = input(f"Asign a new description for {i}: ")
        dict1[i] = int(_) if (i == "price" or i == "quantity") else _
        dict2[i].append(dict1[i])
    list1.append((num, dict1))
    print(f"Current data on the goods is {"*" * 30}")
    for key, value in dict2.items():
        print(f"{key[:25]:>30}: {value}")
    print("*" * 30)
