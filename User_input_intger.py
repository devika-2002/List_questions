                                    # reverse
# enter the number:-4
    # O/P:-[4,3,2,1]
n=int(input("enter the num:-"))
i=1
l=[]
while i<=n:
    l.append(i)
    i=i+1
j=-1
m=[]
while j>=-len(l):
    m.append(l[j])
    j=j-1
print(m)