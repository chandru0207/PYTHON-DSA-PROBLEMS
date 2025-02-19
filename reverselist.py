def reverselist(n):
    rl=n[::-1]
    return rl
out=list(map(int,input("enter the list of elements : ").split()))
print(reverselist(out))
