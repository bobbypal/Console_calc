import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
#operations
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("Type the first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("Type the Second number: "))
        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice = input("Type 'y' to continue calculating with previous calculations or type 'n' for new calculations").lower()

        if choice == "y":
            num1=answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()
