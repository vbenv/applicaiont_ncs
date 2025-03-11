# 1) Ice Americano : 2000 2) Cafe Latte : 3000
drinks = ["Ice Americano", "Cafe Latte"]
prices = [2000, 3000]
total_price = 0
while True:
    menu = input(f"1) {drinks[0]} {prices[0]}  2) {drinks[1]} {prices[1]}  3) Exit : ")
    if menu == "1":
        print(f'{drinks[0]} ordered. Price : {prices[0]} won\n')
        total_price = total_price + prices[0]
    elif menu == "2":
        print(f'{drinks[1]} ordered. Price : {prices[1]} won\n')
        total_price = total_price + prices[1]
    elif menu == "3":
        print("Finish order~")
        break
    else:
        print(f"{menu} menu is not exist. please choose a above menu.")
print(f"Total price : {total_price}")