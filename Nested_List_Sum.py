# a=[4,3,[6,9,1],14,12]
a=[6,2,4,[3,2,8],7,14]
i=0
sum=0
b=[]
while i<len(a):
    if type(a[i])!=list:
        sum=sum+a[i]
    else:
        b.extend(a[i])
        j=0
        s=0
        while j<len(b):
            s=s+b[j]
            j+=1
    i+=1 
totel_sum=sum+s 
print(totel_sum)   
  



