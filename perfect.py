# out=int(input("enter a number: "))
# sum=0
# for i in range(1,out):
#     if(out%i==0):
#         sum+=i
# if(sum==out):
#     print(out,"is a perfect number")
# else:
#     print(out,"is not a perfect number")


# Function to check if a number is perfect
def is_perfect(num):
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 += i
    return sum1 == num

# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Loop through the range and check for perfect numbers
for num in range(start, end + 1):
    if is_perfect(num):
        print(num , "is a Perfect number!")
