def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return x ** 0.5

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Modulus")
print("7. Floor Division")
print("8. Square Root")

choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

if choice == '8':
    num = float(input("Enter number: "))
    print(f"√{num} = {square_root(num)}")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '6':
        print(f"{num1} % {num2} = {modulus(num1, num2)}")
    elif choice == '7':
        print(f"{num1} // {num2} = {floor_division(num1, num2)}")
    else:
        print("Invalid input")
