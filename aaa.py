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
# if  a=="{" or a=="[" or a=="(" or a=="}" or a=="]" or a==")":
if a[i]==count==count1==count2==count3==count4==count5:
    #  count1==count4
     print("true")
else:
  print("false")

  
