while True:
    a = float(input("Введіть перше число: "))
    op = input("Введіть операцію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b != 0:
            print(a / b)
        else:
            print("Ділення на нуль неможливе")
    else:
        print("Невідома операція")

    cont = input("Продовжити? (y/yes для продовження): ").lower()
    if cont not in ("y", "yes"):
        break
