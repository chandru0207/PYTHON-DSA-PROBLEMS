listsum=list(map(int,input("enter a number : ").split()))
out=0
for i in listsum:
    if (i>0):
        out=out+i
    else:
        break
print(out)