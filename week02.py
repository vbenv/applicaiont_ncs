# 1) Ice Americano : 2000 2) Cafe Latte : 3000

prices = [2000, 3000]
while True:
    menu = input(f"1) Ice Americano {prices[0]}  2) Cafe Latte {prices[1]}  3) Exit : ")
    if menu == "1":
        print(f'Ice Americano ordered. Price : {prices[0]} won')
    elif menu == "2":
        print(f'Cafe Latte ordered. Price : {prices[1]} won')
    elif menu == "3":
        print("Finish order~")
        break