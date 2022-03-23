# Magic_squaren=[[25,13,1,19,7],
#             [16,9,22,15,3],
#             [12,5,18,6,24]
#             [8,21,14,2,20]
#             [4,17,10,23,11]]
a=[]
i=0
while i<5:
    b=[]
    b.append(int(input("Enter the number1:-")))
    b.append(int(input("Enter the number2:-")))
    b.append(int(input("Enter the number3:-")))
    b.append(int(input("Enter the number4:-")))
    b.append(int(input("Enter the number5:-")))
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

