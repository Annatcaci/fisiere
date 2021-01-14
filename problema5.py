with open ("numar.txt","r") as f:
    n=f.readline()
with open ("inmultire.txt","w") as f:
    for i in range(1,11):
        x=str(i)+"*"+n+"="+str(i*int(n))
        f.write(str(x))
        f.write("\n")