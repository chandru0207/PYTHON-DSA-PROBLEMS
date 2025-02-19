def sum_list(number):
    out=[]
    var=[lambda number:out+number]
    return out
out1=list(map(int,input("enter the list of numbers:").split()))
print(sum_list(out1))