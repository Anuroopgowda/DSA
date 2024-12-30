def bubble_sort(arr):
    for _ in range(len(arr)):
        swapped=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j + 1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            break
    return arr

arr=[11,25,12,22,64]
print(bubble_sort(arr))