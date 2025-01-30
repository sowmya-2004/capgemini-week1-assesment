class Email:
    emails=[]
    def send(self,email):
        self.emails.append(email)
        print("recieved an email")
class Sms:
    messages=[]
    def send(self,message):
        self.messages.append(message)
        print("recieved an mesage")
class Push:
    pushes=[]
    def send(self,push):
        self.pushes.append(push)
        print("recieved a push")

inp=input("enter email or message or push")
def myfunction(obj,res):
    if(hasattr(obj,"send")):
        obj.send(res)

if(inp=="email"):
    res=input("enter the email")
    e=Email()
    myfunction(e,res)
if(inp=="message"):
    res=input("enter the message")
    e=Sms()
    myfunction(e,res)
if(inp=="push"):
    res=input("enter the push")
    e=Push()
    myfunction(e,res)