# Check if a number is odd or even

try: 
    # Get the user input
    num = int(input("Enter an integer: "))

    # Check if odd or even
    if num % 2 == 0:
        print(f"{num} is even.")

    else:
        print(f"{num} is odd.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")