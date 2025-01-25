def bmicalc(weight,height):
    bmival=weight/(height*height)
    if(bmival<18.5):
        return "Underweight"
    elif(bmival>=18.5 and bmival<=24.9):
        return "Healthy"
    elif(bmival>=25 and bmival<=29.9):
        return "Overweight"
    else:
        return "Obese"
    
weight=float(input("enter weight in kgs"))
height=float(input("enter height in metres"))
condition=bmicalc(weight,height)
print(f"person is {condition}")