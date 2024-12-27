def divide(arr,k):
    k=k%len(arr)
    if k!=0:
        rotate(arr,0,len(arr)-1)
        rotate(arr,0,k-1)
        rotate(arr,k,len(arr)-1)
    return arr

def rotate(arr,left,right):
    
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr



arr=[1,2,3,4,5]
k=2
print(divide(arr,k))