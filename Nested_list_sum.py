# a=[[1,2,3],[3,2,6],[3,5,1]]
# sum=0
# for i in a:
#     print(i)
    
    
a=[[1,2,3]]
sum=0
b=[]
for i in a:
    for j in i:
        sum=sum+i
    b.append(sum)
print(b)