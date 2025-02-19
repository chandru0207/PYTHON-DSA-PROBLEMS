def largest_of_element(n):
    largest=n[0]
    for i in n:
        if i>largest:
            largest=i
    return largest
out=list(map(int,input("enter the list of elements : ").split()))
print(largest_of_element(out))