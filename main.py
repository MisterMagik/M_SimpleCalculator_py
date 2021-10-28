def check_option(numberchoice, a, b):
    match numberchoice:
        case 1:
            print("Sum:", Adding(a, b))
        case 2:
            print("Sum:", Subtraction(a, b))
def main():
    print("Simple Calculator V 1.0")
    print("1. Adding\t 2. Subtraction\n2. Multiplication\t 4.Division")
    choice = input()
    numberone = input("Enter number one: ")
    numbertwo = input("Enter number two: ")
    check_option(choice, numberone, numbertwo)
def Adding(a, b):
    return a + b
def Subtraction(a, b):
    return a - b
def Multiplication(a, b):
    return a * b
def Division(a, b):
    return a / b
main()