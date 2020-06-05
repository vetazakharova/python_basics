class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return f"The sum of two cells is {self.cell + other.cell}"

    def __sub__(self, other):
        return f"The result of subdivision is {self.cell - other.cell}" if self.cell - other.cell > 0 \
            else "Cannot subdivide because there are more units in the first cell then in the second"

    def __mul__(self, other):
        return f"The multiplication result of two cells is {self.cell * other.cell}"

    def __truediv__(self, other):
        return f"The division result of two cells is {round(self.cell / other.cell)}"

    def make_order(self, cells_row):
        row = ''
        for i in range(int(self.cell / cells_row)):
            row += f'{"*" * cells_row} \n'
            row += f'{"*" * (self.cell % cells_row)}'
        return row

cells1 = Cell(40)
cells2 = Cell(5)
print(cells1)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)
