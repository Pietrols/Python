# Write out the operator functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


#add these 4 functions into a dictionary.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


#use dictionary operations to perform the calculations
# print(operations["*"](4, 8))
def calculator():


    should_accumulate = True
num1 = float(input("What is the first number?: "))

while should_accumulate:

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operator: ")
    num2 = float(input("What is the other number?:"))
    calculation = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {calculation}")

    choice = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to start a new calculation: ")

    if choice == "y":
        num1 = calculation
    else:
        should_accumulate = False
        print("\n" * 20)
        calculator()

calculator()
