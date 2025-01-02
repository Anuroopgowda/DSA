def linear_search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return "key found"
    return "key not found"

arr=[11,25,12,22,64]
key=22
print(linear_search(arr,key))