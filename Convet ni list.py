list=[2,4,6,3,8,9,3]
i=0
b=[]
while i<len(list)-1:
    c=[]
    c.append(list[i])
    c.append(list[i+1])
    b.append(c)
    i=i+2
print(b)