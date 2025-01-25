def is_century(year):
    cnt=0
    while(year%10==0):
        cnt+=1
        year=year/10
    if(cnt>=2):
        return True
    else:
        return False
    
def leap_year(year):
    if(is_century(year)):
        if(year%400==0):
            return "leap year"
        else:
            return "Not a leap year"
    elif(year%4==0):
        return "leap year"
    else:
        return "Not a leap year"
year=int(input("enter the year"))
answer=leap_year(year)

print(f"the given year is {answer}")
