num=int(input("enter the number: "))
a,b=0,1
number=[]
while a<=num:
    number.append(a)
    a,b=b,a+b
print(number)
    
    
