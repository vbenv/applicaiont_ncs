drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000, 4900]
amounts = [0] * len(drinks)
total_price = 0
DISCOUNT_THRESHOLD = 10000
DISCOUNT_RATE = 0.1

def apply_discount(price: int):
    """
    If the total amount exceeds a certain standard value, the price is returned reflecting the discount rate.
    Args:
        price (int): pre-discount price
    Returns:
        price (int): discount price
    """
    if price >= DISCOUNT_THRESHOLD:
        return price * (1 - DISCOUNT_RATE)
    return price

# 단일 책임의 원칙 -> print, total_price, amounts를 각각 나눠서 하는 것이 좋긴하나 간단한 예제이므로 합쳐서 진행
def order_process(idx: int):
    """
    Functions that address the beverage order display function, the total cumulative amount calculation and update total amount.

    Args:
        idx (int): list's index number
    """
    # global total_price : 함수 종료된 후에도 total_price에 적용되도록 글로벌 변수 선언
    global total_price
    print(f"{drinks[idx]} ordered. Price : {prices[idx]}won")
    total_price = total_price + prices[idx]
    amounts[idx] += 1

menu_lists = "".join([f'{k+1}) {drinks[k]} {prices[k]} won ' for k in range(len(drinks))])

while True:
    try:    
        menu = int(input(menu_lists + f"{len(drinks) + 1}) Exit : "))
        if len(drinks) >= menu >= 1:
            order_process(menu - 1)
        elif menu == (len(drinks)+1):
            print("Finish order~")
            break
        else:
            print(f"{menu} menu is invalid. please choose from above menu.")
    except ValueError as err:
        print(f"You cannot enter characters. Please enter a valid number.\n{err}.")


print("Product \tPrice\tAmount \tSubtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]}\t{prices[i]}\tx{amounts[i]}\t{prices[i] * amounts[i]}won")


discounted_price = apply_discount(total_price)    
discount_amount = total_price - discounted_price
print(f"Original price : {total_price}won")

if discount_amount > 0:
    print(f"discount amount : {discount_amount}won")
    print(f"Total price after discount : {discounted_price}won")
else:
    print("The discount has not been applied")
    print(f"Total price : {total_price}won")
