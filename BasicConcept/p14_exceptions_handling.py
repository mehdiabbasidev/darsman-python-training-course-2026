try:
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))
    result=num1/num2
    print(f"Result is : {result}")
    open("file11.txt","r")
except ValueError:
    print("Value Error...")
except FileNotFoundError:
    print("File Not Found Error...")
except ZeroDivisionError:
    print("Zero Division Error...")
finally:
    print("The End...")

print("Hello")
