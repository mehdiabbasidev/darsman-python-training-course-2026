correct_username='admin'
correct_password='123'
max_attempts=3

for attempt in range(max_attempts):
    username=input("Enter username :")
    password=input("Enter password :")
    if correct_username==username and correct_password==password :
        print("Login successful...")
        break
    else:
        print("Wrong username or password...")
else:
    print("Account locked...")


