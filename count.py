def out(start,end):
    if start<=end:
        print(start,end=" ")
        out(start+1,end)
start=int(input("enter the start value:"))
end=int(input("enter the end value:"))
out(start,end)