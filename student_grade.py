
def grade(name,marks):
    sum=0
    for i in range(5):
        sum+=marks[i]
    print(f'total marks are {sum}')
    percentage=(sum/5)
    print(f'percentage of marks is{percentage}')
    if(percentage>85):
        print(" grade is O")
    elif(percentage>70):
        print(" grade is A")
    elif(percentage>55):
        print(" grade is B")
    elif(percentage>45):
        print(" grade is C")
    elif(percentage>35):
        print(" grade is D")
    else:
        print("fail")
marks=[]
name=input("enter your name ")
for i in range(1,6):
    n=int(input(f"enter subject {i} marks"))
    marks.append(n)
grade(name,marks)

       
    