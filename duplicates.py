numbers3=[2,2,4,6,3,4,6,1]
n=len(numbers3)
for num in numbers3:
    while(numbers3.count(num)>1):
        numbers3.remove(num)
print(numbers3)