arr=[12,45,345,67,54,61,345,65,23,67,89,4,9,43,23,78,78]
print(arr)

n=len(arr)
for i in range(n-1,0,-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)