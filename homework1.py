class Date:
    def __init__(self, date1):
        self.date1 = str(date1)

    @classmethod
    def to_num(cls, date1):
        day = int(date1[0:2])
        month =int(date1[3:5])
        year = int(date1[6:7])

        return day, month, year

    @staticmethod
    def checking(day, month, year):
        if day >= 1 and day <= 31:
            if month >= 1 and month <=12:
                if year >= 0:
                    return "The date is valid"
                else:
                    return "The input year is not valid"
            else:
                return "The input month is not valid"
        else:
            return "The input day is not valid"

    def __str__(self):
        return f"The current date is {Data.to_num(self.date1)}"

print(Date.to_num("30-01-20"))
print(Date.checking(11, 11, 2022))
print(Date.to_num('11-11-2011'))
print(Date.checking(1, 11, 2000))
