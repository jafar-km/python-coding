import art
print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

Math_operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    print(art.logo)
    no_1 = float(input("What is the first number?"))
    continue_calculation = True
    while continue_calculation:
        for symbol in Math_operations:
            print(symbol)

        chosen_operation = input("Pick an operation: ")
        no_2 = float(input("What is the second number?"))
        result = Math_operations[chosen_operation](no_1, no_2)
        print(f"{no_1} {chosen_operation} {no_2} = {result}")

        previous_answer = result
        new_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
        if new_input == "y":
            no_1 = previous_answer

        else:
            continue_calculation = False
            print("\n" *20)
            calculator()
calculator()