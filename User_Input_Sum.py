a="(){}[]"
i=0
count=0
while i<len(a):
    count+=1
    i=i+1
print(count)

a="{[(}]})"
i=0
count=0
count1=0
count2=0
count3=0
count4=0
count5=0
while i<len(a):
  if a[i]=="{":
    count+=1
  elif a[i]=="[":
    count1=count1+1
  elif a[i]=="(":
    count2+=1
  elif a[i]=="}":
     count3+=1
  elif a[i]=="]":
    count4+=1
  elif a[i]==")":
    count5+=1
  i=i+1
print(count)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
# if  a is a:
#      print("true")
# else:
#   print("false")

  



       


