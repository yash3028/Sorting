def merge(arr,l,m,r):
    temp=[]
    left=l
    right=m+1
    while left<=m and right<=r:
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=m:
        temp.append(arr[left])
        left+=1
    while right<=r:
        temp.append(arr[right])
        right+=1
    for i in range(len(temp)):
        arr[l+i]=temp[i]

def merge_sort(arr,l,r):
    if l>=r:
        return
    m = (l+r)//2
    merge_sort(arr,l,m)
    merge_sort(arr,m+1,r)
    merge(arr,l,m,r)

arr=[3,2,4,1,3]
n=len(arr)
merge_sort(arr,0,n-1)
print(arr)
