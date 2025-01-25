dict={}
def add_items(item,price):
    dict[item]=price
def view_cart():
    print(dict)
def exit():
    print("exit")
def total_price():
    sum=0
    for item in dict:
        sum+=dict[item]
    print(f"total price is:{sum}")

add_items("bread",50)
add_items("milk",20)
add_items("chalk",5)

view_cart()

total_price()

exit()
