# 1. Define the functions needed; add, subtract, multiply and divide
# 2. Print options to the user
# 3. Ask for values
# 4. Call the functions
# 5. Use the while loop to continue the program untilo the user wants to exit
# 6. Give it spaces for neat organization using "\n"


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")     #This is the same as print(a, b)

def subtract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiply(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def divide(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


while True:
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exit")


    choice = input("Input your choice: ")

    if choice == "A" or choice == "a":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)

    elif choice == "B" or choice == "b":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        subtract(a, b)

    elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        multiply(a, b)

    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        divide(a, b)

    elif choice == "E" or choice == "e":
        print("Program Ended")
        quit()