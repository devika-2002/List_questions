list = [10, 11, 12, 13, 14, 17, 18, 19]
# O/P:-  11 , 19
    #    12 , 18
    #    13 , 17
    #    17 , 13
    #    18 , 12
    #    19 , 11
n=len(list)
sum=30
i=0
while i<n:
    j=0
    while j<n:
        if (list[i]+list[j]==sum):
            print(list[i],",",list[j])
        j+=1
    i+=1