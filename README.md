# Week-1-Introduction-To-Python

# Basic Calculator Program

This is a simple Python program that performs basic mathematical operations. The program prompts the user to input two numbers and an operation (addition, subtraction, multiplication, or division) and then displays the result.

## Features
- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second (with a check for division by zero).

## Requirements
- Python 3.x

## How to Use

1. Clone this repository or download the Python script file.
   ```bash
   git clone https://github.com/KabeloMatlakala/Week-1-Intro-To-Python.git
   ```

2. Navigate to the directory containing the script:
  ```bash
  cd basic-calculator
  ```

3. Run the Python program:
  ```bash
  python calculator.py
  ```

4. Follow the prompts:
  Enter the first number.
  Enter the second number.
  Enter the mathematical operation you want to perform (+, -, *, /).
  The program will display the result of the operation.

### Example
  ```bash
  Enter the first number: 10
  Enter the second number: 5
  Enter the operation (+, -, *, /): +
  10.0 + 5.0 = 15.0
  ```

### Error Handling
- If the user tries to divide by zero, the program will display an error message: Error: Division by zero is not allowed.
- If an invalid operation is entered, the program will inform the user that the operation is invalid.
