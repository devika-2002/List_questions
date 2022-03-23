a=[3,9,6,4,8,12,13]
i=0
sum=0
while i<len(a):
    if a[i]%2==0:
       sum=sum+a[i]
    i=i+1
print("even",sum)

