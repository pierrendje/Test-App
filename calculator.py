def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    """Simple calculator with user prompts"""
    print("\n" + "="*40)
    print("       SIMPLE CALCULATOR")
    print("="*40 + "\n")
    
    while True:
        try:
            # Get first number
            num1 = float(input("Enter first number: "))
            
            # Display operations
            print("\nSelect operation:")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            print("5. Exit")
            
            choice = input("\nEnter choice (1/2/3/4/5): ").strip()
            
            if choice == '5':
                print("\nThank you for using the calculator!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select 1, 2, 3, 4, or 5.\n")
                continue
            
            # Get second number
            num2 = float(input("Enter second number: "))
            
            # Perform operation
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            # Display result
            print("\n" + "-"*40)
            if isinstance(result, str):  # Error message
                print(result)
            else:
                print(f"Result: {num1} {operation} {num2} = {result:.2f}")
            print("-"*40 + "\n")
            
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    calculator()