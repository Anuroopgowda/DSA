def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements, if any
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example Usage
array = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", array)
sorted_array = merge_sort(array)
print("Sorted array:", sorted_array)