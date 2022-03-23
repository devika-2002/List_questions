# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]  
# i=1
# count=0
# while i<len(numbers):
#     c=numbers[i]
#     if c>20 and c<40:
#         count=count+1    
#     i=i+1
# print(count)


a=[4,3,[6,9,15],14,12]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
      j=0
      while j<len(a[i]):
        b.append(a[i][j])
        j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)


        