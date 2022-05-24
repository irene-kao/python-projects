def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    keep_calculating = True

    print("\nWelcome to the Calculator")
    num1 = float(input("What's the first number? "))
    for operator in operations:
        print(operator)

    while keep_calculating == True:
        chosen_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        calculation = operations[chosen_operation]
        answer = calculation(num1, num2)
        print(f"{num1} {chosen_operation} {num2} = {answer}")

        keep_going = input("Do you want to keep calculating with the returned value? y or n: ")
        if keep_going == "y":
            num1 = answer
            keep_calculating = True
        else:
            keep_calculating = False
            calculator()
        
calculator()
