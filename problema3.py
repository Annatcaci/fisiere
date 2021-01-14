with open ("globulet.txt","r") as f:
    a=f.readline()
b=int(a)+3
c=(int(a)+int(b))-2
x=int(a)+int(b)+int(c)
with open ("bradut.txt","w") as f:
    f.write(str(x))