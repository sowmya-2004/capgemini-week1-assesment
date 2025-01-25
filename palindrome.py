def palindrome_str(str):
    length=len(str)
    i,j=0,length-1
    while i<j:
        if(str[i]!=str[j]):
            return False
        i+=1
        j-=1
    return True
def palindrome_int(num):
    val=0
    actual=num
    while(num>0):
        val=val*10+num%10
        num//=10
    if(val==actual):
        return True
    else:
        return False

op=input("string or int")
if(op=="string"):
    str=input("enter string")
    if(palindrome_str(str)==True):
        print("given string is palindrome")
    else:
        print("given string is not palindrome")

# if(op=="int"):
#     num=int(input("enter number"))
#     num=str(num)
#     if(palindrome_str(num)==True):
#         print("given number is palindrome")
#     else:
#         print("given number is not palindrome")


if(op=="int"):
    num=int(input("enter number"))
    if(palindrome_int(num)==True):
        print("given number is palindrome")
    else:
        print("given number is not palindrome")
