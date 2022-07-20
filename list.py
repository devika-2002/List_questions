# list=['p','q']
# # ['p1','q1','p2','q2','p3','q3','p4','q4','p5,'q5]
# n=5
# b=[]
# i=1
# while i<len(list)+4:
#     j=0
#     while j<len(list):
#         b.append(list[j]+str(i))
#         j=j+1
#     i=i+1
# print(b)

n=int(input("enter the numer:-"))
i=1
while i<=n:
    if i%2==0:
        print(i,"Postive")
    else:
        print(-i,"Negative")
    i=i+1