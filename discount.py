products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
discount=list(filter(lambda x:x["price"]>=100,products))
print(type(discount))
print(discount)
prices=list(map(lambda x:{"name":x['name'], "price":x['price']*0.8},discount))
print(prices)