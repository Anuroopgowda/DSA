def find(lst):
    if len(lst)==2:
        return min(lst[0],lst[1])
    else:
        first1=max(lst[0],lst[1])
        second1=min(lst[0],lst[1])
        for i in range(2,len(lst)):
            if lst[i]>second1:
                second1=lst[i]
                if second1>first1:
                    second1,first1=first1,second1
    print(second1)
    return second1


lst=[3,4,16,10]
print(find(lst))