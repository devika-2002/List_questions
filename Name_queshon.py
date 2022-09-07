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

# name="My 2 name3e i5s devika2.4"
# i=0
# a=" "
# while i<len(name):
#     if (name[i]>='A' or name[i]>='a') and (name[i]<='Z' or name[i]<='z') or name[i]==" ":
#         a+=name[i]        
#     i=i+1
# print(a.split())
          
# Str = "My 2 nam3e i5s priyanka2.4"
# # output = ["my","name","is","priyanka"]
# s = " "
# for i in Str:
#     if not i.isdigit():
#         s+=i
#         d = s.split()
# print(d)

# name="my name123 devika"
# # outfut=['123']>>>>>>>>>>>>>>????????????
# i=0
# a=" "
# b=''
# while i<len(name):
#     if (name[i]>='A' or name[i]>='a') and (name[i]<='Z' or name[i]<='z') or name[i]==" ":
#         a+=name[i]
#     else:
#         b+=name[i]      
        
#     i=i+1
# print(b.split())


# name="devikakumari123@gmal.come"
# # outfut=['1','2','3']
# i=0
# a=" "
# b=[]
# while i<len(name):
#     z=name[i]
#     if z>='0' and z<='9':
#         b.append(z)        
#     i=i+1
# # print(a.split())
# print(b)

Str = "My 2 nam3e i5s priyanka2.4"
# output = ['23524']
s = " "
for i in Str:
    if i.isdigit():
        s+=i
        d = s.split()
print(d)