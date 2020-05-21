def int_func(str1):
    result = str1.capitalize()
    return result

str_user = input("Write a few words divided by spaces: ").split()
fin_str = ""

for i in str_user:
    fin_str += int_func(i) + " "
    
print(fin_str)
