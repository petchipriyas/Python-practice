# Menu-Driven Python Application

# 1. Pyramid Star Pattern
def pyramid_pattern(n):
    for i in range(1, n + 1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")

        # Print stars
        for j in range(2 * i - 1):
            print("*", end="")

        print()


# 2. Inverted Number Pattern
def inverted_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


# 3. Sum of First N Natural Numbers using Recursion
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


# 4. Power using Lambda
power = lambda base, exponent: base ** exponent


# Main Menu
while True:
    print("\n===== MENU =====")
    print("1. Print Pyramid Star Pattern")
    print("2. Print Inverted Number Pattern")
    print("3. Calculate Sum of First N Natural Numbers")
    print("4. Calculate Power of a Number")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter number of rows: "))
        pyramid_pattern(n)

    elif choice == "2":
        n = int(input("Enter number of rows: "))
        inverted_number_pattern(n)

    elif choice == "3":
        n = int(input("Enter N: "))
        if n < 0:
            print("Please enter a positive number.")
        else:
            result = recursive_sum(n)
            print("Sum of first", n, "natural numbers =", result)

    elif choice == "4":
        base = float(input("Enter base: "))
        exponent = int(input("Enter exponent: "))
        result = power(base, exponent)
        print("Result =", result)

    elif choice == "5":
        print("Program exited successfully.")
        break

    else:
        print("Invalid choice. Please try again.")