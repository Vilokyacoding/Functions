def calculator(a, b, operation):
    """
    Calculator to perform addition and multiplication.

    Parameters:
        a (float): First number.
        b (float): Second number.
        operation (str): 'add' or 'multiply'.

    Returns:
        float: Result of the operation.

    Raises:
        ValueError: If an invalid operation is provided.
    """
    if operation == 'add':
        return a + b
    elif operation == 'multiply':
        return a * b
    else:
        raise ValueError("Invalid operation. Choose 'add' or 'multiply'.")


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation ('add' or 'multiply'): ").strip().lower()
    try:
        result = calculator(num1, num2, op)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)