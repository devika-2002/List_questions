a=[1,2,3,4,23,5,8,6,78]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
print(a)


     