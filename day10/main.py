from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 if n1 > n2 else n2 - n1

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 if n2 != 0 else "Indeterminate operation"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for i in operations:
        print(i)

    while True:
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        calculation = operations[operator]
        result = calculation(num1, num2)

        print(f"{num1} {operator} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation or 'e' to exit: ").lower()
        if choice in ["y", "yes"]:
            num1 = result
        elif choice in ["n", "no"]:
            num1 = int(input("What's the first number? "))
        else:
            break

calculator()