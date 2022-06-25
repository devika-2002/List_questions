# aagr mey a dalu to aayega amiaha aayega O/P:=["amisha"]

name=input("enter the name:-")
a=["amisha","manpreet","rani","rekha"]
i=0
b=[]
while i<len(a):
    if a[i][0] in name:
        b.append(a[i])
    i=i+1
print(b)
        
