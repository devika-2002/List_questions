n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
a=[]
while i<len(n):
    if n[i] not in a:
        a.append(n[i])
    i=i+1
print(a)
