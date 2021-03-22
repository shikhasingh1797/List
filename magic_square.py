magic=[
    [2,7,6],
    [9,5,1],
    [4,3,8]
]
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
length=len(magic)
while i<length:
    a=a+magic[i][0]
    b=b+magic[i][1]
    c=c+magic[i][2]
    d=d+magic[0][i]
    e=e+magic[1][i]
    f=f+magic[2][i]
    g=g+magic[i][i]
    h=h+magic[i][2-i]
    i=i+1
if (a==b==c==d==e==f==g==h):
    print("it is a magic number")
else:
    print("it is not a magic number")