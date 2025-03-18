drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000, 4900]
# amounts = [0, 0, 0]        # Order amounts, 0 : Ice Americano, 1 : Cafe Latte, 2 : Watermelon
amounts = list()
for _ in range(len(drinks)):
    amounts.append(0)
total_price = 0

# 단일 책임의 원칙 -> print, total_price, amounts를 각각 나눠서 하는 것이 좋긴하나 간단한 예제이므로 합쳐서 진행
def order_process(idx: int):
    # global total_price : 함수 종료된 후에도 total_price에 적용되도록 글로벌 변수 선언
    global total_price
    print(f"{drinks[idx]} ordered. Price : {prices[idx]}won")
    total_price = total_price + prices[idx]
    amounts[idx] += 1
    

menu_lists = ''
for k in range(len(drinks)):
    menu_lists += f'{k+1}) {drinks[k]} {prices[k]} won '
    
while True:
    menu = int(input(menu_lists + f"{len(drinks) + 1}) Exit : "))
    if len(drinks) >= menu >= 1:
        order_process(menu - 1)
    elif menu == (len(drinks)+1):
        print("Finish order~")
        break
    else:
        print(f"{menu} menu is not exist. please choose from above menu.")


print("Product \tPrice\tAmount \tSubtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]}\t{prices[i]}\tx{amounts[i]}\t{prices[i] * amounts[i]}")
    
print(f"Total price : {total_price}")
