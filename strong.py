def strong(number):
    digit=str(number)
    fac=list(factorial(int(x)) for x in digit)
    if sum(fac)==number:
        return("strong number")
    else:
        return("not a strong number")
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

out=(int(input("enter the number:")))
print(strong(out))
    