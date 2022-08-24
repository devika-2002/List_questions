a=[[8],[6,87,[54,67]]]
# O/p:- [8,6,87,54,67]
c=[]
i=0
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    c.append(a[i][j][k])
                    k+=1
            else:
                c.append(a[i][j])
            j+=1
    else:
        c.append(a[i])
    i+=1
print(c)

