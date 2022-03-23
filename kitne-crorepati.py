money = [3000, 600000, 324990909, 
        90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
Crorepati=0
Lakhpati=0
Dilwale=0
while i<len(money):
        if money[i]>=100 and money[i]<100000:
                Crorepati=Crorepati+1
        elif money[i]>=100000 and money[i]<10000000:
                Lakhpati=Lakhpati+1
        else:
             Dilwale=Dilwale+1
        i=i+1
print("money in  Crorepati", Crorepati)
print("money in Lakhpati",Lakhpati)
print("money in Dilwale",Dilwale)