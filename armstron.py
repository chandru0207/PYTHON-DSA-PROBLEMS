def arm(n):
    digits=str(n)
    nn=len(digits)
    sumofpower=sum(int(x)**nn for x in digits)
    return sumofpower == n
out=int(input("emter the number:"))
if arm(out):
    print("armstrong number")
else:
    print("not armstrong number")
