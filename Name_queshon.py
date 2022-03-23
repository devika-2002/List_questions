# name="my name is devika"
# # o/p  ["my","name","is","devika"]
# c=[]
# a=" "
# for i in name:
#     if i==" ":
#         c.append(a)
#         a=" "
#     else:
#         a=a+i
# if a:
#     c.append(a)
# print(c)
            
            
# a="my name is devika"           
# i=0
# s=" "
# while i<len(a):
#     if a[i]==" ":
#        b=str(a[i]).replace(" ","-")
#        s=s+b
#     else:
#         s=s+a[i]
#     i+=1
# print(s)

name="My name is devika"
i=0
a=" "
b=[]
while i<len(name):
    if name[i]==" ":
        b.append(a)
        a=" "
    else:
        a=a+name[i]
    i=i+1
if a:
    b.append(a)
print(b)
        
        
    
    