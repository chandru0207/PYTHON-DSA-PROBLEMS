def perfectsq(n):
    if n<0:
        return False
    sq_n=n**0.5
    return sq_n == int(sq_n)
out=(int(input("enter the number:")))
if perfectsq(out):
    print("perfect square")
else:
    print("not a perfect square")