
IsRunning = True
def check_option(numberchoice, numbera, numberb):
    match numberchoice:
        case 1:
            print("Sum: ", Adding(numbera, numberb))

        case 2:
            print("Sum: ", Subtraction(numbera, numberb))
        case 3:
            print("Sum: ", Multiplication(numbera, numberb))
        case 4:
            print("Sum: ", Division(numbera, numberb))

def main():

    while IsRunning != False:
        print("Simple Calculator V 1.0")
        print("1. Adding\t 2. Subtraction\n2. Multiplication\t 4.Division")
        choice = input()
        numberone = input("Enter number one: ")
        numbertwo = input("Enter number two: ")
        check_option(int(choice), int(numberone), int(numbertwo))
def Adding(a, b):
    sum = a + b
    return sum
def Subtraction(a, b):
    return a - b
def Multiplication(a, b):
    return a * b
def Division(a, b):
    return a / b
main()