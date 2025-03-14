# Basic Calculator Program

def calculator():
    # Get user input for the two numbers and the operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation.")
        return

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the calculator function
calculator()
