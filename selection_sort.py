arr=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(arr)
for i in range(n):
    mini=i
    for j in range(i+1,n):
        if arr[mini]>arr[j]:
            mini=j
    arr[i],arr[mini]=arr[mini],arr[i]
print(arr)
