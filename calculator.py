print("Welcome to the python calculator")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    user_choice = int(input("press 1 to add, 2 to subtract, 3 to multiply, 4 to divide "))

    first_number = int(input("enter first number "))

    second_number = int(input("enter second number "))



    if user_choice == 1:
        print(add(first_number, second_number))

    elif user_choice == 2:
        print(subtract(first_number, second_number))

    elif user_choice == 3:
        print(multiply(first_number, second_number))

    elif user_choice == 4:
        if second_number == 0:
            print("You can't divide by zero.")
        else:
            print(divide(first_number, second_number))

    else:
        print("Invalid choice")


    answer = input("continue? y/n")
    answer = answer.lower()
    if answer == "n":
        break