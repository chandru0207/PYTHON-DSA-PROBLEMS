def remove_duplicate(n):
    rd=[]
    for i in n:
        if(i not in rd):
            rd.append(i)
    return rd
out=list(map(int,input("enter the list of elements : ").split()))
print(remove_duplicate(out))
