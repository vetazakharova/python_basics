try:
    file5 = open("file5.txt", "w+")
    numbers = input("write a list of numbers:")
    file5.writelines(numbers)
    list1 = numbers.split()
    print(list1)
    print(sum(map(int, list1)))
except IOError:
    print("Error in the file")
except ValueError:
    print("There has been a value error")
    
