a=[3,9,6,4,8,12,13]
i=0
c=0
Even=0
sum=0
while i<len(a):
    if a[i]%2==0:
       sum=sum+a[i]
       c+=1
       ave=sum/c
    i+=1
print("Sum_Even",sum)
print("Even_count",c)
print("Even_Average",ave)
