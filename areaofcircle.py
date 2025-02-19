def pri(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
out=int(input("enter the number :"))
if pri(out):
    print(out,"is a prime number")
else:
    print(out,"is a not prime number")