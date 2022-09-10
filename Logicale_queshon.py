#1...# Ek user input lena hai  OR  hum jo EK variable me hum store a=2647
# # ye wala number store kr diye  OR o/p :-6 dena cha hiye 

user=input("enter the number")
a="2367"
i=0
b=str(a)
while i<len(user):
    if "6" in user[i] and b[i]:
        print("true")
    else:
        print("false")
        
    i=i+1
       

# #2..# jo hmara a="3456"  diya huaa hai aager ya user ne yhi number diya to 
# # (hum whi number dale to print) hona chahiye true uske aalawa dale to false       
# a="3456"
# n=input("enter the number")
# i=0
# while i<len(a):
#     if n in a:
#         print("true")
#         break 
#     else:
#         print("false")
#         break
#     i=i+1


#3...# Agr hme user ne :Enter the number:-2356 diya to hume O/P:-2000+300+50+6 dega 
# num=int(input("enter the number"))
# a=[]
# i=len(str(num))-1
# for s in str(num):
#     if s !="0":
#         a.append(s+"0"*i)
#     i=i-1
# print("+".join(a))


# #4...# a=[('a',1),('b',4),('z',7),('y',2),('i',5),('j',3),('o',6)] Hai
#    #O/P:-[('a',1),('y',2),('j',3),('b',4),('i',5),('o',6),('z',7)]

# a=[('a',1),('b',4),('z',7),('y',2),('i',5),('j',3),('o',6)]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[j] [1]>a[i][1]:
#             a[i],a[j]=a[j],a[i]
#         j=j+1
#     i=i+1
# print(a)


# #5...# EVEN_Number ka Squre and Uske baad us SQURE KA  SUM krna hai
# # O/P:-[4,16,64]
# # O/P:-[4,7,10]
# a=[2,1,7,4,5,8]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i]*a[i])
#     i=i+1
# print(b)
# d=[]
# c=b
# j=0
# while j<len(c):
#     b=str(c[j])
#     k=0
#     sum=0
#     while k<len(b):
#         sum+=int(b[k])
#         k+=1
#     d.append(sum)
#     j+=1
# print(d)

# #5..# Queshon:-list=['2',4,6,'3',4,'9',3] list hai OR ishka  squre krna hai
# # O/P:- aayega [4,8,36,9,16,81,9]
# list=['2',4,6,'3',4,'9',3]
# i=0
# a=[]
# while i<len(list):
#     if type(list[i])==int:
#         d=int(list[i])**2
#         a.append(d)
#     elif type(list[i])==str:
#         c=int(list[i])**2
#         a.append(c)
#     i=i+1
# print(a)


# list=[1,2,3,4,12,13,5,6]
# i=0
# b=[]
# while i<len(list):
#     c=list[i],list[i+1]
#     b.append(c)
#     i=i+2
# print(b)

# list=[1,2,3,4,11,14,2,1]???????????????????????????????????same
# a=[]
# i=0
# while i<len(list)-1:
#     k=list[i:i+2]
#     a.append(k)
#     i=i+2
# print(a)

# list=[[4,3,4],[6,3,4],[8,1,3]]
# i=0
# while i<len(list):
#     j=0
#     sum=0
#     k=0
#     while j<len(list):
#         sum=sum+list[i][j]
#         j=j+1
#         i=i+1
#     print(sum)

# ##  Queshon list=[1,2,4,5,7,9,11] list hai OR jo missing_number  hai sb dega
# # O/P:-[1,2,3,4,5,6,7,8,10,11] yesha:??
# list=[1,2,4,5,7,9,11]
# i=1
# while i<=len(list):
#     j=0
#     a=[]
#     while j<len(list):
#         if i not in list:
#             list.append(i)
#             list.sort()
#         j=j+1
#     i=i+1
# print(list)

# a=[11,33,50]# ???????????
# # O/P:-# 113350
# i=0
# while i<len(a):
#     print(a[i],end="")
#     i=i+1