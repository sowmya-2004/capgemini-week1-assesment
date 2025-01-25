def kelvin_to(temp):
    celsius=temp-273.15
    fahrenheit=(temp-273)*(9/5)+32
    return [celsius,fahrenheit]
def celsius_to(temp):
    kelvin=temp+273.15
    fahrenheit=(temp)*(9/5)+32
    return [kelvin,fahrenheit]
def fahernheit_to(temp):
    kelvin=(temp-32)*(5/9)+273.15
    celsius=(temp-32)*(5/9)
    return [celsius,kelvin]
op=input("enter temperature type")
temp=int(input("enter temperature"))
if(op=="kelvin"):
    [celsius,fahrenheit]=kelvin_to(temp)
    print(f"celsius-{celsius},fahrenheit-{fahrenheit}")
if(op=="celsius"):
    [kelvin,fahrenheit]=celsius_to(temp)
    print(f"kelvin-{kelvin},fahrenheit-{fahrenheit}")
if(op=="fahrenheit"):
    [celsius,kelvin]=fahernheit_to(temp)
    print(f"celsius-{celsius},kelvin-{kelvin}")

