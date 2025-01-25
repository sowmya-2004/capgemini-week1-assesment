def odd_even(nums):
    odd_list=[]
    even_list=[]
    for num in nums:
        if(num%2==0):
            even_list.append(num)
        else:
            odd_list.append(num)
    print("odd list is ")
    print(odd_list)
    print("even list is")
    print(even_list)

list=[]
n=int(input("size of the list"))
print("enter the numbers")
for i in range(n):
    num=int(input())
    list.append(num)
odd_even(list)
    