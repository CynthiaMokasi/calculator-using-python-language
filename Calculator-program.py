def get_user_name():
    """Prompts the user for their first and last names."""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name

def get_float_input(prompt):
    """Prompts the user for a floating-point number and handles invalid input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

def perform_calculation():
    """Prompts the user for operation and performs the selected calculation."""
    print("\nAvailable operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Exponentiation (**)")

    operation = input("Select an operation (+, -, *, **): ").strip()

    if operation in ['+', '-', '*', '**']:
        print("Enter the first number:")
        num1 = get_float_input("> ")
        
        print("Enter the second number:")
        num2 = get_float_input("> ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '**':
            result = num1 ** num2

        print(f"\nThe result of {num1} {operation} {num2} is: {result}")
        return True
    else:
        print("Invalid operation selected. Please choose one of the available operations.")
        return False

def main():
    """Main function to run the calculator program."""
    print("Welcome to the Python Calculator!")

    # Get user's name
    first_name, last_name = get_user_name()
    print(f"\nHello, {first_name} {last_name}! Let's start calculating.")

    computations = 0
    max_computations = 5

    while computations < max_computations:
        if perform_calculation():
            computations += 1
        else:
            print("Let's try again.")

        if computations < max_computations:
            continue_calculating = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
            if continue_calculating != 'yes':
                break

    print(f"\nYou have performed {computations} computations. Thank you for using the calculator. Goodbye!")

if __name__ == "__main__":
    main()
