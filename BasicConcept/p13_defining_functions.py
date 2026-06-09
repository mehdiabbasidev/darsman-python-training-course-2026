# def print_hello():
#     print("Hello")

# def calc(a:int,b:int):
#     print(a+b)
#     print(a*b)
#     print(a-b)
#     print(a/b)


# def mul(a,b,c):
#     return a*b*c

# def get300():
#     return 3000


# print(mul(10,20,30))
# print(mul(3,6,9))
# print(mul(10,4,8))
# print(mul(12,34,56))


# -------------------------------------
def print_range(start:int,end:int):
    for i in range(start,end+1):
        print(i,end="\t")

# -------------------------------------

sn=int(input("Enter start number : "))      
en=int(input("Enter end number : "))       
if sn>en:
    sn,en=en,sn
    
print_range(sn,en)





