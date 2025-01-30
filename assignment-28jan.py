products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
lis=products.split(" ")
d={}
for word in lis:
    d[word]=lis.count(word)

for x in d:
    print(x," ",d[x])


initial_stock = {"apple": 50,"banana": 100,"orange": 75}
sold_item = {"apple": 10, "banana": 20, "orange": 15}
final_list={}
for x in initial_stock:
    n=initial_stock[x]-sold_item[x]
    final_list[x]=n
print(final_list)
 

sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000}
]

total_sales=0
for x in sales_data:
    total_sales+=x["sales"]

print(total_sales)


number=int(input("enter the mobile number"))
number=str(number)
dic={'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine",'0':"zero"}
for n in number:
    print(dic[n],end=" ")
