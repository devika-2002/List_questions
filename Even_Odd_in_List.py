a=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
c=[]
while i<len(a):
    if i%2==0:
        b.append(a[i])
    elif i%2!=0:
        c.append(a[i])
    i=i+1
print(b,"odd")
print(c,"even")

# a=[3,9,6,4,8,12,13]
# i=0
# while i<len(a):
#     if a[i]%2!=0:
#         print("odd",a[i]*a[i],end=" ")
#     i=i+1