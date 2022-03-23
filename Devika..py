
# num=int(input("enter the number"))
# n=num
# i=0
# j="0"
# a=n%10
# b=num//10
# c=b%10
# print(str(b-c)+j,"+",str(c)+j,"+",a)
# print(a)
# print(b)
# print(c)
  
# list=[2,4,6,3,8,9,3]
# # o/p:-[[2,4],[6,3],[8,9]]
# i=0
# a=[]
# while i<len(list)-1:
#     c=[]
#     c.append(list[i])
#     c.append(list[i+1])
#     a.append(c)
#     i=i+2
# print(a)

# a=[]
# i=0
# while i<len(list)-1:
#     b=list[i:i+2]
#     a.append(b)
#     i=i+2
# print(a)


list=[2,4,6,3,8,9,3]
i=0
b=[]
while i<len(list)-1:
    c=[]
    c.append(list[i])
    c.append(list[i+1])
    b.append(c)
    i=i+2
print(b)



