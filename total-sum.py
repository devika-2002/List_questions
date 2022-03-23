number=30
n = [10, 11, 12, 13, 14, 17, 18, 19]
# o/p:-[[11,19], [12,18],[13,17]]
a=len(n)
sum=30
b=[]
i=0
while i<len(n):
    c=[]
    j=0
    while j<len(n):
        if n[i]+n[j]==number and n[j]>n[i]:
            c.append(n[i])
            c.append(n[j])
            b.append(c)
        j=j+1
    i=i+1
print(b)
    