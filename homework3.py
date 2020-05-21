month = int(input("write a number of a month from 1 to 12: "))

dict1 = {1 : "january", 2 : "februrary", 3 : "march", 4 : "april", 5 : "may", 6 : "june", 7 : "july", 8 : "august", 9 : "september", 10 : "october", 11 : "november", 12 : "december"}
list1 = ["january", "februrary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

for key in dict1:
    if key == month:
        print(f"{month} month is {dict1[key]}")
        print(f"{month} month is {list1[month-1]}")
    else:
        print("Wrong number")
    break
