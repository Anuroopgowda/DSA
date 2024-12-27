# using pointer
'''find duplicates and replace the elements of the same array and then slice it for the result'''
def duplicate(arr):
    slice_count=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[slice_count]=arr[i]
            slice_count+=1
    return arr[:slice_count]


arr=[1, 1, 2, 2, 3, 4]
print(duplicate(arr))

'''will not work if array is emply and the space compx is more'''
# def duplicate(arr):
#     lst=[]
#     lst.append(arr[0])
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[i-1]:
#             lst.append(arr[i])
#     return lst

# arr=[1, 1, 2, 2, 3, 4]
# print(duplicate(arr))

