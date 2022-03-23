a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
sum=0
sum1=0
sum2=0
even=0
odd=0
ave=0
ave1=0
ave2=0
while i<len(a):
    sum2=sum2+a[i]
    ave2=sum2/len(a)
    count=count+1
    if a[i]%2==0:
        even=even+1
        sum=sum+a[i]
        ave=sum/even
    else:
       odd=odd+1
       sum1=sum1+a[i]
       ave1=sum1/odd
    i=i+1
print("total average count",count)
print("total average sum",sum2)
print("average",ave2)
print("totel even number",even)
print("totel even number sum",sum)
print("average of even number",ave)
print("totel odd number",odd)
print("totel odd number sum1",sum1)
print("average of odd number",ave1)


  