# Magic_square=[[8,3,4],
#             [1,5,9],
#             [6,7,2]]
a=[]
i=0
while i<3:
    b=[]
    b.append(int(input("Enter the number1:-")))
    b.append(int(input("Enter the number2:-")))
    b.append(int(input("Enter the number3:-")))
    a.append(b)
    j=0
    column=0
    row=0
    daigonal=0
    l=len(a)
    while j<l:
        row=row+a[i][j]
        column=column+a[j][i]
        daigonal=daigonal+a[j][j]
        j=j+1
    i=i+1
print(column,'column')
print(row,'row')
print(daigonal,'daigonal')
print()
if row==column==daigonal:
    print("This is magic square")
else:
    print("This is not magic square")
print(a)

