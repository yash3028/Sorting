arr=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(arr)
for i in range(1,n):
    index=i
    while index>0 and arr[index-1]>arr[index]:
        temp=arr[index-1]
        arr[index-1]=arr[index]
        arr[index]=temp
        index-=1
print(arr)