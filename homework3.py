class Listcheck:
    def __init__(self, *args):
        self.my_list = []

    def checking(self):
        while True:
            try:
                num = int(input("Input a number and press enter: "))
                self.my_list.append(num)
                print(f"The current list is {self.my_list}")
            except:
                print("Can't process the input, it shouldn't be a string or boolean.")
                cont = input("Do you want to continue? Y/N").casefold()
                if cont == "y":
                    print(check.checking())
                elif cont ==  "n":
                    return f"You exited the programm"
                else:
                    return f"You exited the programm"


check = Listcheck(1)
print(check.checking())
