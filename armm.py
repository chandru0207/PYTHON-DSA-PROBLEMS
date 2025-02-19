def arm(number):
    out=str(number)
    n=len(out)
    sumofpow=sum(int(x)**3 for x in out)
    return sumofpow==number
out1=int(input("enter a number:"))
if arm(out1):
    print("armstrong number")
else:
    print("not armstrong number")
    
