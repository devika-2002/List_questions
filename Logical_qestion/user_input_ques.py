a=int(input("enter the number:-"))
b=int(input("enter the number:-"))
c=int(input("enter the number:-"))
d=int(input("enter the number:-"))
l=[a,b,c,d]
i=0
count=0
while i<len(l)-1:
    if l[i+1]==l[i]+1:
        count+=1
    i=i+1
if count==len(l)-1:
    print("yes")
else:
    print("No")