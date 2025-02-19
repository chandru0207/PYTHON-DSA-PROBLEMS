def secondlarge(n):
    secondlar=n[1]
    for i in n:
        if i>secondlar:
            secondlar=i
    return secondlar
out=list(map(int,input("enter the numbers:").split()))
print(secondlarge(out))