def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        print(i,min_index)
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[11,25,12,22,64]
print(selection_sort(arr))
