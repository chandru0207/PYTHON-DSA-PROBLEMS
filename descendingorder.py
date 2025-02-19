def descending_order(n):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]<n[j]:
                n[i],n[j]=n[j],n[i]
    return n
out=list(map(int,input("enter the the list : ").split()))
print(descending_order(out))