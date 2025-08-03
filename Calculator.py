#Defining operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

#Mapping operations to functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#Getting user input
print("Enter the first number:")
first_number = float(input())

print("Enter the second number:")
second_number = float(input())

print("Enter the operation (+, -, *, /):")
operation = input()

#Perform the operation using the dictionary
if operation in operations:
    try:
        result = operations[operation](first_number, second_number)
        #Displaying the result
        print(f"The result of {first_number} {operation} {second_number} is {result}")
    except ValueError as e:
        print("Error:", e)
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
