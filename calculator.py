
num1=int(input("ENTER NUMBER= "))
num2=int(input("ENTER NUMBER= "))
operation=input("PLEASE PRVIDE THE OPERATION")

if operation == "+":
    print(f"The addition of two numbers is {num1+num2}")

if operation == "-":
    print(f"The subtraction of two numbers is {num1-num2}")

if operation == "*":
    print(f"The multiplication is {num1*num2}")

if operation == "/":
    print(f"The division is {num1/num2}")

else:
    print("OPERATOR NOT VALID")

print("END")
