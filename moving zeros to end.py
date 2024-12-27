# brute force method
'''count no of zeros and append at the end'''

# two pointers
def move_zeros_to_end(arr):
    non_zero_index = 0  # Tracks the position to place non-zero elements

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1

    return arr

# Input
arr = [1,9,0,0,1]
print(move_zeros_to_end(arr))

