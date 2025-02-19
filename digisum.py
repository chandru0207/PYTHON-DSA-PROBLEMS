# a=123
# out=0
# while(a>0):
#     digit=a%10
#     out=out+digit
#     a=a//10
# print(out)

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return((n%10)+sum_of_digits(n//10))
out=int(input("enter a number : "))
print(sum_of_digits(out))  # Output: 6