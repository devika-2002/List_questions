list=['p','q']
# ['p1','p1','p2','p2','p3','p3','p4','p4','p5,'p5,]
n=5
b=[]
i=1
while i<len(list)+4:
    j=0
    while j<len(list):
        b.append(list[j]+str(i))
        j=j+1
    i=i+1
print(b)
