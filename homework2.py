class Division:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def division(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = Division(10, 100)
print(Division.division(10, 0))
print(Division.division(10, 0.1))
print(div.division(100, 0))
print(div.division(12, 4))
