numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
count=0
while i<len(numbers):
    n=numbers[i]
    if n>20 and n<40:
        count=count+1
    i=i+1
print("number between 20 and  40 :-",count)