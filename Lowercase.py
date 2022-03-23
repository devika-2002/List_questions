a="i LOVE you "
i=0
capital=0
small=0
while i<len(a):
    if a[i].isupper():
        capital+=1
    elif a[i].islower():
        small+=1
    else:
        pass
    i=i+1
print("uppercase",capital)
print("lowercase",small) 