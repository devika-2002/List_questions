n=input("Enter the bracket:-")
i=0
if n[i]=="(" and n[i+1]==")" :
    print("true")
elif n[i]=="[" and n[i+1]=="]":
    print("true")
elif n[i]=="{" and n[i+1]=="}":
    print("true")
elif n[i]=="[" and n[i+1]=="]" :
    print("true")

else:
    print("false")