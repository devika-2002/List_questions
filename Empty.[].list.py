a=[1,2,[],4,5,[],6]
i=0
b=[]
while i<len(a):
    if a[i] !=[]:
        b.append(a[i])
    i=i+1
print(b)