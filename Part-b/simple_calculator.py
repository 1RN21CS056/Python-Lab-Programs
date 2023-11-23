while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'quit' to end the program")
    
    user_choice = input(":")

    if user_choice == "quit":
        break

    if user_choice in ("+", "-", "*", "/"):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if user_choice == "+":
            result = num1 + num2
        elif user_choice == "-":
            result = num1 - num2
        elif user_choice == "*":
            result = num1 * num2
        elif user_choice == "/":
            if num2 == 0:
                print("Cannot divide by zero")
                continue
            result = num1 / num2

        print("Result:", result)
    else:
        print("Invalid input")
