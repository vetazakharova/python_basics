class Worker:
    def __init__ (self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit" : profit, "bonus" : bonus}

class Position (Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name (self):
        return self.name + " " + self.surname

    def get_total_income (self):
        return self._income.get("profit") + self._income.get("bonus")

worker1 = Position("Maria", "Uzumaki", "Ninja", 100000, 10000)
print(worker1.get_full_name())
print(worker1.position)
print(worker1.get_total_income())
