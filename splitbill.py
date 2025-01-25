def split_bill(people,bill,tip_percentage):
    bill=bill+(tip_percentage/100)*bill
    splitbill=bill/people
    return splitbill
people=int(input("enter no.of people"))
bill=int(input("enter total bill"))
tip_percentage=int(input("enter tip percentage"))
value=split_bill(people,bill,tip_percentage)
print(f"each person need to pay{value}")