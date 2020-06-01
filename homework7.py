import json
dict1 = {}
dict2 = {}
profit = 0
i = 0
with open("file7.txt", "r") as file7:
    for line in file7:
        name, firm, earnings, loss = line.split()
        dict1[name] = int(earnings) - int(loss)
        if dict1.setdefault(name) >= 0:
            profit += dict1.setdefault(name)
            i += 1
    if i>= 0:
        profit_average = profit / i
        print("Average profit is " + str(profit_average))
    else:
        print("All firms work with a loos, there is no profit")
    dict2 = {'average profit': round(profit_average)}
    dict1.update(dict2)
    print(dict1)
with open("file7.json", "w") as file7:
    json.dump(dict1, file7)
    js_str = json.dumps(dict1)
