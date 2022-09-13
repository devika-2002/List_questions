s='AABCAAADA'
i=0
while i<len(s):
    print(s[i]+s[i+2])
    if i==1:
        # print(s[i]+s[i+2])
        print(s[i+4]+s[i+6])
        break
    i=i+1
    
    

