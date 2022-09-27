# list=[1,2,3,4,5,6]
# o/p[[6,1],[5,2],[4,3]]

# list=[[1,2],[3,4],[5,6]]
# i=0
# sum=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         sum=sum+list[i][j]
#         j=j+1
#     # print(sum)
#     i=i+1
# print(sum)


# # o/p:-17
# a=[[3,8,6]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)


a=["A","B"]
i=0
emti_list=[]
while i<len(a):
    j=1
    while j<=5:
        emti_list.append(a[i]+str(j))
        j=j+1
    i=i+1
print(emti_list)
    

# o/p  
# My
# name
# is 
# devika
# a="my name is devika"
# i=0
# while i<len(a):
#     if a[i]==" ":
#         print()
#     else:
#         print(a[i],end="")
#     i=i+1