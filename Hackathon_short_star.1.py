array=["Lets","all","go","on","holiday","somewhere","very","cold"]
# o/p:-'L***e***t***s'
array.sort()
i=0
b=""
while i<len(array[0]):
    a=array[0][i]+"***"
    b=b+a
    i+=1
print(b[0:-3])
