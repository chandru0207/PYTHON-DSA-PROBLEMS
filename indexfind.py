def find_end_index(W1, W2):
    start_index = W1.find(W2)  # Find where W2 starts in W1
    if start_index == -1:
        return -1  # If W2 is not found in W1, return -1
    return start_index + len(W2) - 1  # Calculate the end index

# Sample Input
W1 = input().strip()
W2 = input().strip()

# Output the result
print(find_end_index(W1, W2))
