# Function to add two numbers
def addition(a, b):
    return a + b

# Function to multiply two numbers
def multiplication(a, b):
    return a * b

# Accept two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for the operation choice
print("Choose the operation:")
print("1. Addition")
print("2. Multiplication")
choice = int(input("Enter your choice (1 or 2): "))

# Perform the selected operation using conditional statements
if choice == 1:
    result = addition(num1, num2)
    print("The sum is:", result)
elif choice == 2:
    result = multiplication(num1, num2)
    print("The product is:", result)
else:
    print("Invalid choice. Please enter 1 or 2.")
