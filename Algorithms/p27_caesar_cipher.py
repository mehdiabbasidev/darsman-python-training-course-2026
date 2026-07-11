
def show_menu():
    print("1. Encrypt")
    print("2. Dncrypt")
    print("3. Exit")
    print("===================================")



while True:
    show_menu()
    cmd_number=int(input("Enter cmd number : "))
    if cmd_number==3:
        break

    text=input("Enter text: ")
    shift=int(input("Enter shift number : "))
    shift%=26
    if cmd_number==1:
        shift*=-1

    res=""
    for ch in text:
        if ch.isalpha():
            res+=chr(ord(ch) + shift)
        else:
            res+=ch

    print(res)
