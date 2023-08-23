def sort012(arr,n):
    low,mid=0,0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==2:
            arr[high],arr[mid]=arr[mid],arr[high]
            high-=1
        else:
            mid+=1
    return arr
a=[2,1,2,2,2,2,2,0,0,1,2,0,1,0,1,0,0,0,2,0,2,2,1]
l=len(a)
a=sort012(a,l)
print("Sorted array:",a)
