def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)
out=(int(input("enter a num :")))
print(facto(out))
