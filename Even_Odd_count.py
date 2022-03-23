a=[1,2,3,4,5,6,7,8,9]
i=0
b=0
c=0
while i<len(a):
    if a[i]%2==0:
        b=b+1
    else:
        c=c+1
    i=i+1
print("count_Even",b)
print("count_Odd",c)
