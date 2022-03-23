# enter the number:-devika
# enter the number:kumari
# enter the number:rajbanshi
# O/P:-D.K.rajbanshi

a=input("enter the number:-")
b=input("enter the number:-")
c=input("enter the number:-")
d=" "
i=0
while i<len(a) and i<len(b):
    if a[i]==a[0] and b[i]==b[0]:
        cap=a[i].upper()
        cap1=b[i].upper()   
        d+=cap+"."+cap1
    i=i+1
print(d+"."+c)

