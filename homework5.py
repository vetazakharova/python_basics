# print("Если вы хотите прервать программу нажмите")
# str_user = input("Введите строку числел разделённых пробелом: ").split()
def my_func():
    result = 0
    while True:
        if input("Если вы хотите прервать программу нажмите 'Q': ").upper() == "Q":
            break
        str_user = input("Введите строку числел разделённых пробелом: ").split()
        for i in str_user:
            if i == "Q" or i == "q":
                break
            result += int(i)
        print(result)

my_func()
