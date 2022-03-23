array=[1,2,3,4,5,6,7,8,9]
# O/P:-[2,4,6,8]: lenth :-4
i=0
a=[]
b=0

while i<len(array):
    if array[i]%2==0:
        a.append(array[i])
        b=len(a)
    i=i+1
print("even number are",a)
print("length of array",b)

