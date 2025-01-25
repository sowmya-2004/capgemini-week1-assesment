def is_prime(n):
    if(n<=1):
        return False
    if(n==2):
        return True
    for i in range(2,n//2):
        if(n%i==0):
            return False
    return True

def rangeof_prime(start,end):
    list=[]
    for i in range(start,end+1):
        if(is_prime(i)):
            list.append(i)
    return list

start=int(input("enter starting of rage"))
end=int(input("end of range"))
answer=rangeof_prime(start,end)
print("prime numbers in range are")
print(answer)