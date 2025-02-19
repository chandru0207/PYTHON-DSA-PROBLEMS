n = list(map(int, input("Enter numbers separated by space: ").split()))  
new = [x for x in n if x % 2 == 0]  
print("Even numbers:", new)
