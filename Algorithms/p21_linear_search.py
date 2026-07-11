arr=[12,45,345,67,23,9,0,345,7689,90]
x=int(input("Enter number for search : "))

res=-1
for i in range(len(arr)):
    if arr[i]==x:
        res=i
        break

if res != -1:
    print(f"Found at index {res}")
else:
    print("Not found...")
