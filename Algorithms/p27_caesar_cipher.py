
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
    if cmd_number==2:
        shift*=-1

    res=""
    for ch in text:
        if ch.isalpha():
            if 'a'<=ch and ch<='z':
                res+=chr((ord(ch) - ord('a')+ shift) % 26 + ord('a'))
            else:
                res+=chr((ord(ch) - ord('A')+ shift) % 26 + ord('A'))
        else:
            res+=ch

    print(res)
