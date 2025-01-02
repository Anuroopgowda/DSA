def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    right=[y for y in arr if y>pivot]
    middle=[z for z in arr if z==pivot]

    return quicksort(left)+middle+quicksort(right)

arr = [38, 27, 43, 3, 9, 82, 10]
print(quicksort(arr))