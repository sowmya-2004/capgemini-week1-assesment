def second(list):
    first=-1e9
    next=-1e9
    for num in list:
        if(num>first):
            next=first
            first=num
        if(num>next and num<first):
            next=num
    return next
    
list=[]
n=int(input("size of the list"))
if(n>2):
    print("enter the numbers")
    for i in range(n):
        num=int(input())
        list.append(num)
    second_large=second(list)
    print(f"second largest is{second_large}")
else:
    print("invalid")
