a= [[3,4,5,6],[4,6],[14],[7,8,9,3]]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type (a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    b.append(a[i][j][k])
                    k=k+1
            else:
                b.append(a[i][j])
            j=j+1
    else:
        b.append
    i=i+1
print(b)