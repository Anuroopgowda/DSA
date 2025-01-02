def binary_search(arr,key,left,right):

    while left<right:
        mid=(left+right)//2

        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return binary_search(arr,key,left,mid)
        else:
            return binary_search(arr,key,mid,right)
    return "not found"


arr=[2,23,45,65,109,220]
key=0
left=0
right=len(arr)
print(binary_search(arr,key,left,right))