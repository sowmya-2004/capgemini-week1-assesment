def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
def reverse_pattern(n):
    while(n>0):
        print(n*"*")
        n-=1
n=int(input("number  "))
print("pattern")
pattern(n)
print(" ")
print("Reverse pattern")
reverse_pattern(n)
