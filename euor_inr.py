prices=[3000,56000,45000,2300]
def inrto_us():
    res_us= map(lambda x:x*0.012,prices)
    print(f"inr in  usd is{list(res_us)}")

def inrto_euro():
    res_euro=map(lambda x:x*0.011,prices)
    print(f"inr in euro is{list(res_euro)}")

inrto_us()
inrto_euro()
