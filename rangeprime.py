def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:        
            return False
        return True
start=int(input("enter the stratting number:"))
end=int(input("enter the ending number:"))
for i in range(start,end+1):
    if prime(i):
        print(i)