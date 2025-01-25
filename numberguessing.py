import random
generate_num=random.randint(1,100)
guess=int(input("enter guess number between 1 and 100"))
if(guess==generate_num):
    print("Success")
elif(generate_num-guess<10):
    print("too low")
else:
    print("too high")