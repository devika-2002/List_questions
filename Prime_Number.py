
# a=[1,2,3,4,5,6]
# prime=0
# i=0
# while i<len(a):
#     if prime%a[i]==1:
#         prime=prime+1
#     i=i+1
# print(prime)


a=[1,2,3,5,8,4]
i=0
while i<len(a):
    j=1
    count=0
    while j<=a[i]:
        if a[i]%j==0:
            count+=1
        j+=1
    if count==2:
        print(a[i],"It is a prime number")
    else:  
        print(a[i],"is not a prime number")
    i+=1