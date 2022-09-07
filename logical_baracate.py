a="(){}[]"
n=input("Enter the bracket:-")
i=0
if n[i]=="(" and n[i+1]==")" and(n[i] and n[i+1]) in a:
    print("true")
elif n[i]=="[" and n[i+1]=="]" and(n[i] and n[i+1]) in a:
    print("true")
elif n[i]=="{" and n[i+1]=="}" and(n[i] and n[i+1]) in a:
    print("true")
elif n[i]=="[" and n[i+1]=="]" and(n[i] and n[i+1]) in a:
    print("true")

else:
    print("false")