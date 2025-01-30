list1=[1,4,7,2,9,5]
result=list(filter(lambda x:x%2==0,list1))
evens=map(lambda x:x*2,result)
ans=list(evens)
ans.sort()
print(ans)