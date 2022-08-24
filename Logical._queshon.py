
# o/p:-[[6,1],[5,2],[4,3]] aayega
list=[1,2,3,4,5,6]
a=[]
i=0
j=-1
while i<len(list)/2:
    a.append(list[j])
    a.append(list[i])
    i=i+1
    j=j-1
print(a)
 