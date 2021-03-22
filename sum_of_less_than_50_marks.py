students_marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,9]
length=len(students_marks)
index=0
sum=0
sum1=0
while index<len(students_marks):
    if students_marks<50:
        sum=sum+students_marks[index]
    else:
        sum=sum+students_marks[index]
    index=index+1
print("total marks less than 50 = ",sum)
print("totalmarks more than 50 = ",sum1)

