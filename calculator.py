def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def get_number(message):
    while True:
        try:
            return int(input(message))
        except:
            print("Please enter a valid number")

while True:
    print("""
    ====================
    Python Calculator
    ====================

    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    """)
    try:
        user_choice = int(input("Choose an operation: "))
    except:
        print("Please enter a valid number")
        continue

    if user_choice == 5:
        break
    
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")

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