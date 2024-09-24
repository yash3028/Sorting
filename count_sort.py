arr=[2,5,3,0,2,3,0,3]
n=max(arr)
count=[0]*(n+1)
res=[0]*len(arr)
for i in arr:
    count[i]+=1
for i in range(1,n+1):
    count[i]=count[i-1]+count[i]
for i in range(len(arr)-1,-1,-1 ):
    res[count[arr[i]]-1]=arr[i]
    count[arr[i]]-=1
print(res)