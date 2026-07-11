arr=[4,12,16,19,23,29,34,48,54,63,69,71,90,150,158,192,240]
x=int(input("Enter number for search : "))

left=0
right=len(arr)-1
res=-1

while(left<=right):
    mid=(left+right)//2
    if arr[mid]==x:
        res=mid
        break
    elif arr[mid]<x:
        left=mid+1
    else:
        right=mid-1

if res != -1:
    print(f"Found at index {res}")
else:
    print("Not found...")