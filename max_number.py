# num=[12,34,63,87,27,109,70,96,50]
# i=0
# x=0
# while i!=len(num):
#     if x<num[i]:
#         x=num[i]
#     i=i+1
# print(x)
num=[122,34,63,87,27,109,70,196,50]
z=len(num)
max1=num[0]
max2=num[1]
i=0
while i<z:
    if num[i]>max1:
        max2=max1
        max1=num[i]
    elif max1 >num[i]>max2:
        max2=num[i]
    i=i+1
print("maxium number is = ",max1,"second maximum number is = ",max2)