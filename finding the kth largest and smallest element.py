'''using inbuilt sort function'''
# def k_element(arr,k):
#     arr.sort()
#     lst=[]
#     lst.append(arr[k-1])
#     lst.append(arr[len(arr)-k])
#     return lst

'''using quickselect technique'''
def quickselect(arr, k):
    # Base case: When the array has only one element
    if len(arr) == 1:
        return arr[0]

    # Choose a pivot (here we use the middle element)
    mid = len(arr) // 2
    pivot = arr[mid]

    # Partition the array into left, middle, and right
    left_half = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right_half = [x for x in arr if x > pivot]

    # Determine where the k-th element lies
    if k <= len(left_half):
        # It's in the left half
        return quickselect(left_half, k)
    elif k <= len(left_half) + len(middle):
        # It's in the middle (pivot itself)
        return pivot
    else:
        # It's in the right half
        return quickselect(right_half, k - len(left_half) - len(middle))

# Example Usage
arr = [11, 25, 12, 22, 64]
k = 4
print("Kth smallest element:", quickselect(arr, k))
