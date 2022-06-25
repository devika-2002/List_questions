# list=[1,2,3,4,5,6]
# o/p[[6,1],[5,2],[4,3]]

list=[[1,2],[3,4],[5,6]]
i=0
sum=0
while i<len(list):
    j=0
    while j<len(list[i]):
        sum=sum+list[i][j]
        j=j+1
    # print(sum)
    i=i+1
print(sum)
