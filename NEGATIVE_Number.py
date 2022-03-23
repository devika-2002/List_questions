list1=[-4,5,-1,0,-15]
i=0
b=[]
while i<len(list1):
    if list1[i]<0:
        b.append(list1[i])
    i+=1
print(b)
