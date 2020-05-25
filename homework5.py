from itertools import count
from itertools import cycle

for i in count(int(input("Write a start number for your count: "))):
    if i > 40:
        break
    else:
        print(i)

list1 = [2, 4, 6]
c = 0
for i in cycle(list1):
    if c > 10:
        break
    print(i)
    c += 1
