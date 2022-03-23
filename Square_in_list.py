# list=[3,4,9,6]
# i=0
# while i<len(list):
#     print(list[i]*list[i],end=" , ")
#     i=i+1

#5...# EVEN_Number ka Squre and Uske baad us SQURE KA  SUM krna hai
# O/P:-[4,16,64]
# O/P:-[4,7,10]
a=[2,1,7,4,5,8]
i=0
b=[]
while i<len(a):
    if a[i]%2==0:
        b.append(a[i]*a[i])
    i=i+1
print(b)
d=[]
c=b
j=0
while j<len(c):
    b=str(c[j])
    k=0
    sum=0
    while k<len(b):
        sum+=int(b[k])
        k+=1
    d.append(sum)
    j+=1
print(d)


