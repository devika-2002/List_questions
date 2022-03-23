marks = [[78, 76, 94, 86, 88],
         [91, 71, 98, 65, 76],
         [95, 45, 78, 52, 49]]
i=0
while i<len(marks):
    j=0
    sum=0
    avg=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        avg=sum/len(marks[i])
        j=j+1
    i=i+1
print("avg of element",avg)