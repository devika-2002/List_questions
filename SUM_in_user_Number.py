i=input("enter the number------  ")
a=int(i)
sum=0
while a>0:
    sum=sum+a%10
    a=a//10
print("sum of total",sum)