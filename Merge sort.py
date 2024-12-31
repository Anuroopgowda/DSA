# merge sort
'''It is used to divide the arr till the array size is 1 and then
pass the left half and right half array to func(MERGE) to sort and combine then
then it will again return the array to the recursive function'''
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2

    left_half=mergesort(arr[:mid])
    right_half=mergesort(arr[mid:])

    return merge(left_half,right_half)

def merge(left,right):
    result=[]
    i,j=0,0 # pointer

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1

    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    print(left,right,"===>",result)
    return result

arr=[43,27,38,3,9,82,10]
print(mergesort(arr))