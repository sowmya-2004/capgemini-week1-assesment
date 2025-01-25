def strength(str):
    countsp=0
    countdig=0
    countup=0
    countlow=0
    if(len(str)<8):
        return "weak"
    for chars in str:
        if(chars>='a' and chars<='z'):
            countlow+=1
        elif(chars>='A' and chars<='Z'):
            countup+=1
        elif((chars>="!" and chars<='/') or (chars>="{" and chars<='~') or (chars>=':' and chars<='@')):
            countsp+=1
        else:
            countdig+=1
           
    
    if(countsp==0 or countdig==0):
        return "weak"
    if(countup==0 or countlow==0):
        return "weak"
    return "strong"

str=input("enter string")
print(f"pssword strength is{strength(str)}")