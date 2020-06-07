class StorageMachines:
    def __init__(self, name, price, items, pages):
        self.name = name
        self.price = price
        self.items = items
        self.pages = pages
        self.storage = []
        self.my_unit = {"Name of the item" : self.name, "Price of the item" : self.price, "Number of items" : self.items}

    def inputing(self):
        try:
            unit = input("The name of the item: ")
            unit_p = int(input("The price of the item: "))
            unit_q = int(input("The quantity of the item: "))
            unit_desc = {"Name of the item" : unit, "Price of the item" : unit_p, "Number of items" : unit_q}
            self.my_unit.update(unit_desc)
            self.storage.append(self.my_unit)
            print(f"The current list of items: {self.storage}")
        except:
            return "Data input error"

        let = input("To exit press 'q', to continue press enter ").casefold()
        if let == "q":
            return "You exited the programm"
        else:
            return StorageMachines.inputing(self)

class Printer(StorageMachines):
    def printing(self):
        return f"Printing something {self.pages} pages"

class Scanner(StorageMachines):
    def scanning(self):
        return f"Scanning something {self.pages} pages"

class Copymachine(StorageMachines):
    def copying(self):
        return f"Copying something {self.pages} pages"


item1 = Printer("Hp", 12000, 20, 30)
item2 = Scanner("Samsung", 8000, 24, 10)
item3 = Copymachine("LG", 9000, 8, 12)
print(item1.inputing())
print(item1.printing())
print(item3.copying())
print(item2.scanning())
