def show_menu():
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdra")
    print("4. Exit")

#-----------------------------------------------------------  
def deposit(amount):
    balance+=amount
    print("Deposit successful...")  

#-----------------------------------------------------------  
def withdrw(amount):
    if amount<=balance:
        balance-=amount
        print("Withdrw successful...")
    else:
        print("Not enough balace...")

#-----------------------------------------------------------  
correct_password="123"
balance=2000000

user_password=input("Enter password : ")

if correct_password==user_password:
    while True:
        show_menu()
        cmd_number=int(input("Enter cmd number : "))
        if cmd_number==1:
            print(f"Your balance is :{balance}")
        elif cmd_number==2:
            amount=int(input("Enter deposit amount : "))
            deposit(amount)
        elif cmd_number==3:
            amount=int(input("Enter withdrw amount : "))
            withdrw(amount)
        elif cmd_number==4:
            break
else:
    print("Wrong password...")
