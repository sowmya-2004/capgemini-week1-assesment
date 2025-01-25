'''Atm simulation'''
current_balance=1000
def check_balance():
    
      return current_balance
def deposit(balance):
      global current_balance
      current_balance=current_balance+balance
      return current_balance
def withdraw(balance):
      global current_balance
      current_balance-=balance
      return current_balance
def atm():
      operation=input("enter the operation needed to be performed")
      if(operation=="check balance"):
        available=check_balance()
        print(f"available balance is {available}")
      elif(operation=="deposit balance"):
           amount=int(input("enter the amount to deposit "))
           available=deposit(amount)
           print(f"credited amount is{amount}, total available balance is{available}")
      elif(operation=="withdraw"):
           amount=int(input("enter the balance to withdraw "))
           if(amount<=current_balance):
               available=deposit(amount)
               print(f"withdrawn amount is {amount}, total available balance is {available}")
      else:
           print("invalid operation")
n=int(input("no.of operations to be performed"))
for i in range(n):
      atm()
      
