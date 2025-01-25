age=int(input("enter age"))
salary=int(input("enter salary"))
credit_score=int(input("enter credit score"))
if(age<21):
    print("loan is rejected")
    print("underage for loan sanctioning")
elif(salary<30000):
    print("loan is rejected")
    print("salary is less than required for sanctioning loan")
elif(credit_score<500):
    print("loan is rejected")
    print("credit score is less than required")
else:
    print("loan is approved")