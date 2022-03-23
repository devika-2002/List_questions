#1..# 34-27 kiya tho 7 Aaya
# # esi 6-4 tho 2 aya 
# # esi 7-3 kita tho 4 aya
# a=[34,26,6,4,7,3]
# i=0
# d=[]
# c=a[i+1]
# while i<len(a)-1:
#     c=a[i+1]
#     b=a[i]-c
#     d.append(b)
    
#     i=i+2
# print(d)


#2..# a="asdfghjklasdfgasdfg"
# # o/p:-['a','s','d','f','g','h','j','k','l']
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)

# b='aaabbbcccddd'
# # O/P:-['a','b','c','d']
# i=0
# a=[]
# while i<len(b):
#     if b[i] not in a:
#       a.append(b[i])
#     i=i+1
# print(a)


#3..# Queshon:- a=9119 hai or outfut aana chahiye O/P:-811181 aayega
# a=9119
# b=str(a)
# i=0
# while i<len(b):
#     print(int(b[i])**2 ,end="")
#     i=i+1

# #4..Queshon hai list=["abc",'xyz','aba','1221'] O/P:-2 aayega q ki mera list me 
# # do hi same=same hai Like:['aba','1221']

# list=["abc",'xyz','aba','1221']
# i=0
# count=0
# while i<len(list):
#     if list[i][0]==list[i][-1]:
#         count=count+1
#     i=i+1
# print(count)


# Q.5.$#     
# list=['hello','world','this','is','great']
##O/P:-'hello world this is great'
    #   ye simple me 
# i=0
# string=""
# while i<len(list):
#     string=string+" "+list[i]
#     i+=1
# print("'"+string+"'")

        #  NESTED me Ye wala
# i=0
# str=""
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         if list[i][j]==list[i][0]:
#             x=str+list[i]
#             str+=list[i]+" "
#         j=j+1
#     i=i+1
# print("'"+x+"'")

#2..# Queshon:-list=[2,4,6,3,8,9,3]OR output aana chahiye # 
# yesha aana chahiye # O/P:-[[2,4],[6,3],[8,9]]

# list=[2,4,6,3,8,9,3]
# # O/P:-[[2,4],[6,3],[8,9]]
# i=0
# b=[]
# while i<len(list)-1:
#     c=[]
#     c.append(list[i])
#     c.append(list[i+1])
#     b.append(c)
#     i=i+2
# print(b)    