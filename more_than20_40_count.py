num=[50,40,23,70,56,12,25,10,7]
length=len(num)
i=0
count=0
while i<length:
    if num[i]>20 and num[i]<40:
        count=count+1
    i=i+1
print("numbers between 20 and 40 =",count)