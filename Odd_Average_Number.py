a=[3,9,6,4,8,12,13]
i=0
c=0
odd=0
sum=0
while i<len(a):
    if a[i]%2!=0:
       sum=sum+a[i]
       c+=1
       avg=sum/c
    i+=1
print("sum_odd",sum)
print("odd_count",c)
print("odd_average",avg)