student_names=["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]

def names():
    lone_names=list(filter(lambda x:len(x)>6,student_names))
    print(lone_names)

names()