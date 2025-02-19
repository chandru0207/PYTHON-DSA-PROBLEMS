# # Calculate the sum of the first n natural numbers using the formula n * (n + 1) / 2.
# n = int(input("enter the number : "))
# n=[]
# # rt=0
# # for i in range(1,n+1):
# #     rt = rt + i
# # print("sum of first n natural numbers is ",rt)
# print (n)

# Example: Taking input as a space-separated list
user_input = input("Enter a list of items separated by spaces: ")
input_list = user_input.split()
even_sum=0
odd_sum=0
for i in input_list:
    i=int(i)
    if (i % 2 == 0):  # Check if number is even
        even_sum += i
    else:  # If number is odd
        odd_sum += i
print(even_sum)
print(odd_sum)
