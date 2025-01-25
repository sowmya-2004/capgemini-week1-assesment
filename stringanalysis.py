str=input("enter a string")
vowels=0
consonants=0
specialchar=0
digits=0
set={'a','e','i','o','u','A','I','E','O','U'}
for word in str:
    if(word in set):
         vowels+=1
    elif(word>='a' and word<='z' or word>='A' and word<='Z'):
        consonants+=1
    elif((word>="!" and word<='/') or (word>="{" and word<='~') or (word>=':' and word<='@')):
        specialchar+=1
    else:
        digits+=1
print(f"no.of vowels: {vowels}")
print(f"no.of consonants: {consonants}")
print(f"no.of specialchar: {specialchar}")
print(f"no.of digits: {digits}")

        