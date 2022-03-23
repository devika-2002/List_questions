Magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(Magic_square):
    j=0
    row=0
    c=0
    d=0
    while j<len(Magic_square[i]):
        row=row+Magic_square[i][j]
        c=c+Magic_square[j][i]
        d=d+Magic_square[j][j]
        j=j+1
    i=i+1
if row==c==d:   
    print("This is magic_square")
else:
    print("This is not a magic_square")
print(c)
print(row)
print(d)


# Magic_square=[[8,3,4],
#             [1,5,9],
#             [6,7,2]]
# i=0
# a=0
# b=0
# c=0
# while i<len(Magic_square):
#     a=a+Magic_square[i][0]
#     b=b+Magic_square[i][1]
#     c=c+Magic_square[i][2]
#     i=i+1
#     print(a,b,c)
# if a==b==c:
#     print("magic_squre")
# else:
#     print("not is Magic_square")