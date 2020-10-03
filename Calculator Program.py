#simple calculator
def add(x, y):#adds two numbers
    return x + y
def subtract(x, y):#subtracts two numbers
    return x - y
def multiply(x, y):#multiplies two numbers
    return x * y
def divide(x, y):#divides two numbers
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")# Take input from the user
    if choice in ('1', '2', '3', '4'):# Check if choice is one of the four options
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
