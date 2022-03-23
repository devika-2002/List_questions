# list=["devika",3,11,"divya",2.5]
# a=[]
# b=[]
# c=[]
# i=0
# while i<len(list):
#     if type(list[i])==str:
#         a.append(list[i])
#     elif type(list[i])==int:
#         b.append(list[i])
#     elif type(list[i])==float:
#         c.append(list[i])
#     i=i+1
# print(a)
# print(b)
# print(c)


list=["devika",12, 3.1,"divya",2.1,22,"nikita",2,2.3]
a=[]
b=[]
c=[]
i=0
while i<len(list):
    if type(list[i])==str:
        a.append(list[i])
    elif  type(list[i])==int:
        b.append(list[i])
    elif type(list[i])==float:
        c.append(list[i])
    i=i+1
print(a)
print(b)
print(c)
