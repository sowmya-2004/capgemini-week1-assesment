str=input("enter the string")
set={" "}
list=str.split(" ")
for word in list:
   set.add(word)

for word in set:
    print(f"occurences of {word} is {str.count(word)}")



