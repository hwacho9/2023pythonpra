playing = True

# add your code here!


def sum(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


while playing == True:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))

    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n")
    if operation == "+":
        print(sum(a, b))
    elif operation == "-":
        print(sub(a, b))
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        print(a/b)
    elif operation == "exit":
        break
