Magic_square=[[8,3,4],
            [1,5,9],
            [6,7,2]]
i=0
while i<len(Magic_square):
    row=0
    coulm=0
    j=0
    while j<len(Magic_square):
        row=row+Magic_square[i][j]
        coulm=coulm+Magic_square[j][i]
        d=0
        while d<len(Magic_square):
            d1=0
            d2=0
            c=0
            while c<len(Magic_square):
               d1=d1+Magic_square[d][c]
               d2=d2+Magic_square[c][d]
               d1=d2
               c=c+1
            d=d+1
        j=j+1
    i=i+1
print(row)
print(coulm)
print(d1)
if coulm==row==d1:
    print("it is a magic square")
else:
    print("not a mag")
