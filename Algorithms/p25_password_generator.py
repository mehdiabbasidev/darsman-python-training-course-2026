import random

# letters=""
# for i in range(ord('a'),ord('z')+1):
#     letters+=chr(i)
# print(letters)

# letters=""
# for i in range(ord('A'),ord('Z')+1):
#     letters+=chr(i)
# print(letters)

# numbers=""   
# for i in range(ord('0'),ord('9')+1):
#     numbers+=chr(i)


letters="abcdefghijklmnopqrstuvwxyz"
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="@#_*%^&"

all_char=letters+numbers+symbols

print(all_char)

length=int(input("Enter password length : "))

password=""
for i in range(length):
    password+=random.choice(all_char)

print(f"Password : {password}")
