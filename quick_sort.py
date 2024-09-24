def quick_sort(arr,lb,ub):
    if lb<ub:
        mid=subarr(arr,lb,ub)
        quick_sort(arr,lb,mid-1)
        quick_sort(arr,mid+1,ub)

def subarr(arr,lb,ub):
    pivot=arr[lb]
    start=lb
    end=ub
    while start<end:
        while arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    
    arr[lb],arr[end]=arr[end],arr[lb]  
    return end

arr=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(arr)
quick_sort(arr,0,n-1)
print(arr)
