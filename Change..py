l= [-2,0,78,-48,9,6]
# O/p:- [-48,-2,0,6,9,78]
i=0
while i<len(l):
	j=i+1
	while j<len(l):
		if (l[i]>l[j]):
			temp=l[i]
			l[i]=l[j]
			l[j]=temp
		j=j+1
	i=i+1
print(l)
