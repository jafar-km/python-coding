def add(n1, n2):
    return n1 + n2
calc_no_1 = add


def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

Math_operations = {
    "addition" : [add(4,8)],
    "subtraction" : [subtract(4,8)],
    "multiplication" : [multiply(4,8)],
    "division" : [divide(4,8)]
}
print(Math_operations)


